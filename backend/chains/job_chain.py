"""
job_chain.py

LangChain pipeline for converting a Job Description
into a structured Job object.
"""

from langchain_core.prompts import ChatPromptTemplate

from services.gemini_service import llm

from models.job_model import Job

from prompts import JOB_ANALYZER_PROMPT


structured_llm = llm.with_structured_output(Job)


prompt = ChatPromptTemplate.from_template(
    JOB_ANALYZER_PROMPT
)


chain = prompt | structured_llm


def analyze_job(job_description: str):

    result = chain.invoke(
        {
            "job_description": job_description
        }
    )

    return result