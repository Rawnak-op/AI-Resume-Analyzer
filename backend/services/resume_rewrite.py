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

Rewrite ONLY these sections:

- Professional Summary
- Project Descriptions
- Experience Descriptions

Do NOT rewrite Education, Skills, Certifications or Personal Information.

==================================================
RULES
==================================================

- Never invent projects.
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
    
    content = response.content.strip()
    if not content:
        content = "⚠️ **AI Generation Failed or Blocked.**\nThe model returned an empty response. This usually happens if the AI's safety filters were triggered by something in the job description, or if the model failed to identify any sections to rewrite based on the strict instructions."
        
    return content