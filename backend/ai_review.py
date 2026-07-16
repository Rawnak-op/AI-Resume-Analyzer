from google import genai
from config import GEMINI_API_KEY

# Paste your Gemini API key here
client = genai.Client(
    api_key=GEMINI_API_KEY
)


def review_resume(
    resume_text,
    job_description,
    missing_skills,
    ats_score
):

    prompt = f"""
You are an ATS resume reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

ATS Score:
{ats_score}

Missing Skills:
{", ".join(missing_skills)}

Your task:

1. Give 5 resume improvement suggestions.
2. Mention which missing skills should be added.
3. Suggest better project descriptions.
4. Suggest improvements for ATS.
5. Keep the response concise.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text