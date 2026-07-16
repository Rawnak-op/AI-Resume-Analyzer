"""
job_analyzer.py

Uses Gemini to understand a Job Description.

Instead of hardcoding skill weights, the LLM extracts:

- Role
- Required skills
- Preferred skills
- Optional skills
- Minimum experience
- Keywords

Returns structured JSON.
"""

import json

from google import genai

from config import GEMINI_API_KEY
from prompts import JOB_ANALYZER_PROMPT


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def analyze_job(job_description: str):

    prompt = JOB_ANALYZER_PROMPT.format(
        job_description=job_description
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Gemini sometimes wraps JSON in ```json ... ```
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:

        result = json.loads(text)

        return result

    except Exception:

        print("Gemini returned invalid JSON:\n")
        print(text)

        return {

            "role": "Unknown",

            "required_skills": [],

            "preferred_skills": [],

            "optional_skills": [],

            "minimum_experience": "",

            "keywords": [],

            "summary": ""

        }