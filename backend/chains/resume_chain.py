"""
resume_chain.py

Converts a resume into a Resume object using LangChain.
"""

from langchain_core.prompts import ChatPromptTemplate

from services.gemini_service import llm

from models.resume_model import Resume

from prompts import RESUME_PARSER_PROMPT


structured_llm = llm.with_structured_output(Resume)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", RESUME_PARSER_PROMPT),
        ("human", "{resume_text}")
    ]
)

chain = prompt | structured_llm


def parse_resume(resume_text: str):

    result = chain.invoke(

        {
            "resume_text": resume_text
        }

    )

    return result