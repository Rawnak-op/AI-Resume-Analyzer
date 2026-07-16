import shutil

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_text_from_pdf

from embeddings import get_embedding
from utils.similarity import calculate_similarity

from chains.resume_chain import parse_resume
from chains.job_chain import analyze_job

from ats.analyzer import ATSAnalyzer

from services.resume_rewrite import rewrite_resume


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
    """

    # Extract PDF text
    resume_text = extract_text_from_pdf(
        resume_path
    )

    # Parse Resume
    resume = parse_resume(
        resume_text
    )

    # Parse Job Description
    job = analyze_job(
        job_description
    )

    # Embeddings
    resume_embedding = get_embedding(
        resume_text
    )

    job_embedding = get_embedding(
        job_description
    )

    similarity = calculate_similarity(
        resume_embedding,
        job_embedding
    )

    # ATS
    analyzer = ATSAnalyzer(
        resume,
        job,
        similarity
    )

    ats = analyzer.analyze()

    return (
        resume_text,
        resume,
        job,
        ats
    )


# ==========================================================
# ATS Analysis
# ==========================================================

@app.post("/match")
async def match_resume(

    resume: UploadFile = File(...),

    job_description: str = Form(...)

):

    save_path = f"../resumes/{resume.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(
            resume.file,
            buffer
        )

    resume_text, resume_obj, job_obj, ats = analyze_resume_pipeline(
        save_path,
        job_description
    )

    return ats.model_dump()


# ==========================================================
# Resume Rewrite
# ==========================================================

@app.post("/rewrite")
async def rewrite(

    resume: UploadFile = File(...),

    job_description: str = Form(...)

):

    save_path = f"../resumes/{resume.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(
            resume.file,
            buffer
        )

    resume_text, resume_obj, job_obj, ats = analyze_resume_pipeline(
        save_path,
        job_description
    )

    rewritten = rewrite_resume(
        resume_text,
        job_description,
        ats
    )

    return {
        "rewritten_resume": rewritten
    }