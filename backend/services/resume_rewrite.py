from langchain_core.prompts import ChatPromptTemplate

from services.gemini_service import llm


prompt = ChatPromptTemplate.from_template(
"""
You are an expert resume writer and ATS optimization specialist.

You are given:

1. Resume
2. Job Description
3. ATS Analysis

==================================================
RESUME
==================================================

{resume}

==================================================
JOB DESCRIPTION
==================================================

{job}

==================================================
ATS ANALYSIS
==================================================

ATS Score:
{score}

Missing Required Skills:
{missing_skills}

Strengths:
{strengths}

Weaknesses:
{weaknesses}

==================================================
YOUR TASK
==================================================

You must output the ENTIRE, FULL resume from top to bottom in beautiful Markdown format. Do not truncate or omit anything.

You must REWRITE and OPTIMIZE these specific sections based on the ATS Analysis:
- Professional Summary
- Project Descriptions
- Experience Descriptions (if any)

CRITICAL: You must COPY AND PASTE the following sections EXACTLY as they appear in the original resume. Do NOT omit them!
- Name and Contact Information (Email, Phone, GitHub, Address)
- Education (including CGPA and dates)
- Technical Skills
- Certifications / Interests / Hobbies

==================================================
RULES
==================================================

- Output a fully formatted Markdown document. Use `#` for the name, `##` for section headers, and `-` for bullet points.
- Bold key technologies or metrics inside the bullet points.
- Never invent projects or work experience.
- Never invent work experience.
- Never invent achievements.
- Never invent technologies.
- Never invent certifications.
- Never invent numbers or percentages.
- Only improve wording, formatting and readability.
- Naturally include important keywords from the Job Description.
- Use ATS-friendly language.
- Every bullet should start with a strong action verb.
- Keep every statement truthful.

==================================================
OUTPUT FORMAT
==================================================


Return ONLY valid Markdown.

Use EXACTLY the following format.

# **Professional Summary**

Write a concise 2-4 line professional summary.

# **Projects**

## **1. Project Name**

**Tech Stack:** Technology 1, Technology 2, Technology 3

- Bullet 1
- Bullet 2
- Bullet 3

## **2. Project Name**

**Tech Stack:** Technology 1, Technology 2

- Bullet 1
- Bullet 2
- Bullet 3

# **Experience**

## **1. Company Name**

**Role:** Software Engineer

**Duration:** Jan 2025 - Present

- Bullet 1
- Bullet 2
- Bullet 3

## **2. Company Name**

**Role:** Research Intern

**Duration:** May 2024 - Aug 2024

- Bullet 1
- Bullet 2
- Bullet 3

# **Skills**

## **Programming Languages**

- Python
- C++
- Java

## **Web & Backend**

- FastAPI
- React.js
- REST APIs

## **AI / Machine Learning**

- PyTorch
- LangChain
- Sentence Transformers

## **Databases & Tools**

- SQL
- Git
- GitHub
- Docker

==================================================
FORMATTING RULES
==================================================

- Return ONLY Markdown.
- Do NOT wrap the response inside triple backticks.
- Use '#' for main headings.
- Use '##' for every Project and Experience.
- Number every Project (1., 2., 3...).
- Number every Experience (1., 2., 3...).
- Make ALL section headings bold.
- Make every Project name bold.
- Make every Experience title bold.
- Make "Tech Stack", "Role", and "Duration" bold.
- Use bullet points for achievements.
- Every bullet should start with a strong action verb.
- Use concise, ATS-friendly language.
- Do NOT generate any explanations.
- Output ONLY the rewritten resume.
"""
)

chain = prompt | llm


def rewrite_resume(

    resume_text,

    job_description,

    ats_analysis

):

    response = chain.invoke(

        {

            "resume": resume_text,

            "job": job_description,

            "score": ats_analysis.total_score,
            "missing_skills": ", ".join(ats_analysis.missing_required),
            "strengths": "\n".join(ats_analysis.strengths),
            "weaknesses": "\n".join(ats_analysis.weaknesses)
        }
    )
    
    raw_content = response.content
    if isinstance(raw_content, list):
        # Gemini sometimes returns a list of content blocks
        text_parts = []
        for block in raw_content:
            if isinstance(block, dict) and "text" in block:
                text_parts.append(block["text"])
            else:
                text_parts.append(str(block))
        content = "\n".join(text_parts).strip()
    else:
        content = str(raw_content).strip()
        
    if not content:
        content = "⚠️ **AI Generation Failed or Blocked.**\nThe model returned an empty response."
        
    return content