"""
section_score.py
"""

def calculate_section_score(resume):

    total = 6

    score = 0

    if resume.summary:
        score += 1

    if len(resume.skills):
        score += 1

    if len(resume.projects):
        score += 1

    if len(resume.experience):
        score += 1

    if len(resume.education):
        score += 1

    if len(resume.certifications):
        score += 1

    percentage = score / total * 100

    return {

        "score": percentage

    }