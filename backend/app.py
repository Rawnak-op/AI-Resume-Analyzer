import shutil
import os
import tempfile

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_text_from_pdf

from embeddings import get_embedding
from utils.similarity import calculate_similarity

from chains.resume_chain import parse_resume
from chains.job_chain import analyze_job

from ats.analyzer import ATSAnalyzer

from services.resume_rewrite import rewrite_resume

from cache import get_cached_ats, set_cached_ats

RESUME_DIR = os.path.join(tempfile.gettempdir(), "resumes")
os.makedirs(RESUME_DIR, exist_ok=True)

app = FastAPI()

# ----------------------------
# CORS
# ----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# Helper Function
# ==========================================================

def analyze_resume_pipeline(
    resume_path: str,
    job_description: str
):
    """
    Runs the complete ATS pipeline.

    Cache flow (Layer 3 — Full ATS result):
      1. Extract raw PDF text.
      2. Check Redis for a cached ATS result keyed on (resume_text, jd_text).
      3. On cache miss, run all sub-pipelines (each of which has its own
         inner cache layers for embeddings and LLM extraction).
      4. Store the final ATS result in Redis before returning.
    """

    # Extract PDF text (always needed to compute the cache key)
    resume_text = extract_text_from_pdf(resume_path)

    # --- Layer 3: Cache HIT — skip everything ---
    cached_ats = get_cached_ats(resume_text, job_description)
    if cached_ats is not None:
        from models.ats_model import ATSAnalysis
        return (
            resume_text,
            None,   # resume obj not needed by caller
            None,   # job obj not needed by caller
            ATSAnalysis(**cached_ats)
        )

    # --- Cache MISS: run the full pipeline ---

    # Parse Resume (Layer 2 cache inside parse_resume)
    resume = parse_resume(resume_text)

    # Parse Job Description (Layer 2 cache inside analyze_job)
    job = analyze_job(job_description)

    # Embeddings (Layer 1 cache inside get_embedding)
    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_description)

    similarity = calculate_similarity(resume_embedding, job_embedding)

    # ATS scoring (deterministic — fast, no cache needed at this level)
    analyzer = ATSAnalyzer(resume, job, similarity)
    ats = analyzer.analyze()

    # --- Store full ATS result in Redis ---
    set_cached_ats(resume_text, job_description, ats)

    return (
        resume_text,
        resume,
        job,
        ats
    )


# ==========================================================
# ATS Analysis
# ==========================================================

from fastapi.responses import JSONResponse

@app.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        save_path = os.path.join(RESUME_DIR, resume.filename)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        resume_text, resume_obj, job_obj, ats = analyze_resume_pipeline(
            save_path,
            job_description
        )
        return ats.model_dump()
    except Exception as e:
        import traceback
        return JSONResponse(status_code=400, content={"error": str(e), "traceback": traceback.format_exc()})


# ==========================================================
# Resume Rewrite
# ==========================================================

@app.post("/rewrite")
async def rewrite(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    ats_json: str = Form(...)
):
    try:
        import json
        from models.ats_model import ATSAnalysis

        save_path = os.path.join(RESUME_DIR, resume.filename)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Extract text directly, skipping the heavy AI analysis pipeline!
        resume_text = extract_text_from_pdf(save_path)

        ats = ATSAnalysis(**json.loads(ats_json))

        rewritten = rewrite_resume(
            resume_text,
            job_description,
            ats
        )
        return {"rewritten_resume": rewritten}
    except Exception as e:
        import traceback
        return JSONResponse(status_code=400, content={"error": str(e), "traceback": traceback.format_exc()})
