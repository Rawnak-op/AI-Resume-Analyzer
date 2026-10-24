"""
resume_chain.py

Converts a resume into a Resume object using LangChain.
"""

from langchain_core.prompts import ChatPromptTemplate

from services.gemini_service import llm

from models.resume_model import Resume

from prompts import RESUME_PARSER_PROMPT

from cache import get_cached_llm, set_cached_llm, resume_key


structured_llm = llm.with_structured_output(Resume)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", RESUME_PARSER_PROMPT),
        ("human", "{resume_text}")
    ]
)

chain = prompt | structured_llm


def parse_resume(resume_text: str) -> Resume:
    """
    Parses raw resume text into a structured Resume object.

    Cache flow:
      1. Check Redis for a cached Resume JSON (TTL: 24h).
      2. On cache miss, invoke Gemini via LangChain.
      3. Store the result in Redis before returning.
    """

    key = resume_key(resume_text)

    # --- Layer 2: Cache HIT ---
    cached = get_cached_llm(key)
    if cached is not None:
        return Resume(**cached)

    # --- Cache MISS: call Gemini ---
    result = chain.invoke({"resume_text": resume_text})

    # --- Store in cache ---
    set_cached_llm(key, result)

    return result
