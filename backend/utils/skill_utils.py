import re

from data.skill_synonyms import SKILL_SYNONYMS


def normalize_skill(skill: str):

    skill = skill.lower().strip()

    skill = re.sub(r"\s+", " ", skill)

    skill = skill.replace("-", " ")

    skill = skill.replace("_", " ")

    if skill in SKILL_SYNONYMS:
        skill = SKILL_SYNONYMS[skill]

    return skill