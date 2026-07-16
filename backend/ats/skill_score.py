"""
skill_score.py

Evidence-based skill scoring.
"""

from ats.evidence_builder import build_skill_index
from utils.skill_utils import normalize_skill

CATEGORY_WEIGHT = {
    "required": 0.70,
    "preferred": 0.20,
    "optional": 0.10
}


def evidence_score(evidence):

    score = 0

    if evidence["mentioned_in_skills"]:
        score += 1

    score += len(evidence["projects"]) * 2

    score += len(evidence["experience"]) * 3

    score += len(evidence["certifications"]) * 2

    return score


def category_score(job_skills, evidence_index):

    if not job_skills:

        return {
            "score": 100,
            "matched": [],
            "missing": []
        }

    matched = []
    missing = []

    obtained = 0

    max_per_skill = 8

    for skill in job_skills:

        key = normalize_skill(skill)

        if key in evidence_index:

            matched.append(skill)

            obtained += min(
                evidence_score(
                    evidence_index[key]
                ),
                max_per_skill
            )

        else:

            missing.append(skill)

    maximum = len(job_skills) * max_per_skill

    score = obtained / maximum * 100

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }


def calculate_skill_score(resume, job):

    evidence = build_skill_index(resume)

    required = category_score(
        job.required_skills,
        evidence
    )

    preferred = category_score(
        job.preferred_skills,
        evidence
    )

    optional = category_score(
        job.optional_skills,
        evidence
    )

    final = (

        CATEGORY_WEIGHT["required"] * required["score"]

        +

        CATEGORY_WEIGHT["preferred"] * preferred["score"]

        +

        CATEGORY_WEIGHT["optional"] * optional["score"]

    )

    return {

        "score": round(final, 2),

        "required_score": round(
            required["score"],
            2
        ),

        "preferred_score": round(
            preferred["score"],
            2
        ),

        "optional_score": round(
            optional["score"],
            2
        ),

        "matched_required": required["matched"],

        "missing_required": required["missing"],

        "matched_preferred": preferred["matched"],

        "missing_preferred": preferred["missing"],

        "matched_optional": optional["matched"],

        "missing_optional": optional["missing"]

    }