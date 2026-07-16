"""
quality_score.py
"""

import re


ACTION_VERBS = [

    "developed",
    "built",
    "implemented",
    "designed",
    "optimized",
    "created",
    "improved",
    "trained",
    "engineered"

]


def calculate_quality_score(resume):

    text = ""

    text += resume.summary + " "

    for project in resume.projects:
        text += project.description + " "

    for exp in resume.experience:
        text += exp.description + " "

    text = text.lower()

    score = 0

    # Action verbs
    verbs = 0

    for verb in ACTION_VERBS:

        if verb in text:

            verbs += 1

    score += min(verbs,5)

    # Numbers

    numbers = len(
        re.findall(r"\d+",text)
    )

    score += min(numbers,5)

    percentage = score/10*100

    return {

        "score":percentage

    }