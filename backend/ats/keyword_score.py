"""
keyword_score.py

Calculates keyword overlap between
resume and job description.
"""

from utils.skill_utils import normalize_skill


def calculate_keyword_score(resume, job):

    resume_keywords = set()

    # Skills
    for skill in resume.skills:
        resume_keywords.add(
            normalize_skill(skill.name)
        )

    # Projects
    for project in resume.projects:
        for tech in project.technologies:
            resume_keywords.add(
                normalize_skill(tech)
            )

    # Experience
    for exp in resume.experience:
        for tech in exp.technologies:
            resume_keywords.add(
                normalize_skill(tech)
            )

    job_keywords = set()

    for skill in job.required_skills:
        job_keywords.add(
            normalize_skill(skill)
        )

    for skill in job.preferred_skills:
        job_keywords.add(
            normalize_skill(skill)
        )

    for keyword in job.keywords:
        job_keywords.add(
            normalize_skill(keyword)
        )

    if len(job_keywords) == 0:

        return {
            "score":100,
            "matched":[],
            "missing":[]
        }

    matched = list(
        resume_keywords & job_keywords
    )

    missing = list(
        job_keywords - resume_keywords
    )

    score = len(matched)/len(job_keywords)*100

    return {

        "score":round(score,2),

        "matched":matched,

        "missing":missing

    }