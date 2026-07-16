"""
project_score.py

Semantic project relevance scoring.
"""

from embeddings import get_embedding
from utils.similarity import calculate_similarity


def calculate_project_score(resume, job):

    if len(resume.projects) == 0:

        return {
            "score": 0,
            "best_project": None,
            "project_scores": []
        }

    # Create one JD text
    job_text = (
        job.summary
        + " "
        + " ".join(job.required_skills)
        + " "
        + " ".join(job.preferred_skills)
    )

    job_embedding = get_embedding(job_text)

    scores = []

    for project in resume.projects:

        project_text = (
            project.title
            + " "
            + project.description
            + " "
            + " ".join(project.technologies)
        )

        project_embedding = get_embedding(project_text)

        similarity = calculate_similarity(
            project_embedding,
            job_embedding
        )

        scores.append(
            {
                "title": project.title,
                "score": similarity
            }
        )

    best = max(scores, key=lambda x: x["score"])

    final = best["score"] * 100

    return {

        "score": round(final, 2),

        "best_project": best,

        "project_scores": scores

    }