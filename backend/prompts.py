"""
prompts.py

Stores all Gemini prompts used by the application.
"""

# ====================================================
# JOB ANALYZER
# ====================================================

JOB_ANALYZER_PROMPT = """
You are an expert technical recruiter.

Analyze the following Job Description.

Job Description:

{job_description}

Return ONLY valid JSON.

Schema:

{{
    "role": "",

    "required_skills": [],

    "preferred_skills": [],

    "optional_skills": [],

    "minimum_experience": "",

    "keywords": [],

    "summary": ""
}}

Rules:

1. Do not explain anything.

2. Return ONLY JSON.

3. No markdown.

4. No ```json.

5. Extract technical skills only.
"""

# ====================================================
# AI RESUME REVIEW
# ====================================================

RESUME_REVIEW_PROMPT = """
You are an ATS Resume Reviewer.

Resume:

{resume}

Job Description:

{job}

ATS Score:

{score}

Missing Skills:

{missing}

Return ONLY valid JSON.

Schema:

{{
    "strengths": [],

    "improvements": [],

    "missing_skills": [],

    "project_suggestions": []
}}

Rules:

Only return JSON.

No markdown.

No explanation.
"""


RESUME_PARSER_PROMPT = """
You are an expert resume parser.

Your task is to extract structured information from the resume.

Extract:

- Name
- Email
- Phone
- Summary
- Skills
- Projects
- Experience
- Education
- Certifications
- Achievements

Instructions:

For every skill include:

- skill name
- source
- confidence

For each experience extract:

- company
- role
- duration
- start_date
- end_date
- employment_type
- technologies used
- description

If unavailable leave empty.

If information is missing, leave the field empty.

Do not hallucinate.

Use only information present in the resume.
"""