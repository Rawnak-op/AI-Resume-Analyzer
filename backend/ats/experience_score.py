"""
experience_score.py

Computes experience score.
"""

import re


def extract_required_years(text):

    """
    Extract required years from JD.
    Examples:
    '2 years'
    '3+ years'
    'Minimum 1 year'
    """

    if not text:
        return 0

    match = re.search(r"(\d+)\s*\+?\s*year", text.lower())

    if match:
        return int(match.group(1))

    return 0


def extract_resume_years(resume):

    """
    Very simple heuristic.

    Count:
    Internship ≈ 0.5 year
    Project ≈ 0.5 year
    Full-time ≈ 1 year
    """

    total = 0.0

    for exp in resume.experience:

        role = (
            exp.role.lower()
            if exp.role
            else ""
        )

        emp = (
            exp.employment_type.lower()
            if exp.employment_type
            else ""
        )

        if "intern" in role or "intern" in emp:

            total += 0.5

        elif "project" in emp:

            total += 0.5

        else:

            total += 1.0

    return total


def calculate_experience_score(

    resume,

    job

):

    required = extract_required_years(

        job.minimum_experience

    )

    resume_years = extract_resume_years(

        resume

    )

    # No experience required
    if required == 0:

        return {

            "score":100,

            "resume_years":resume_years,

            "required_years":0

        }

    ratio = min(

        resume_years / required,

        1.0

    )

    return {

        "score":round(

            ratio * 100,

            2

        ),

        "resume_years":resume_years,

        "required_years":required

    }