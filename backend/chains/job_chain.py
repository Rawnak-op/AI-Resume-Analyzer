"""
job_chain.py

LangChain pipeline for converting a Job Description
into a structured Job object.
"""

from langchain_core.prompts import ChatPromptTemplate

from services.gemini_service import llm

from models.job_model import Job

from prompts import JOB_ANALYZER_PROMPT

from cache import get_cached_llm, set_cached_llm, job_key


structured_llm = llm.with_structured_output(Job)

prompt = ChatPromptTemplate.from_template(JOB_ANALYZER_PROMPT)

chain = prompt | structured_llm


def analyze_job(job_description: str) -> Job:
    """
    Parses a raw job description into a structured Job object.

    Cache flow:
      1. Check Redis for a cached Job JSON (TTL: 24h).
      2. On cache miss, invoke Gemini via LangChain.
      3. Store the result in Redis before returning.
    """

    key = job_key(job_description)

    # --- Layer 2: Cache HIT ---
    cached = get_cached_llm(key)
    if cached is not None:
        return Job(**cached)

    # --- Cache MISS: call Gemini ---
    result = chain.invoke({"job_description": job_description})

    # --- Store in cache ---
    set_cached_llm(key, result)

    return result
