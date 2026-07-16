"""
Builds a Skill Evidence Index from the parsed resume.
"""

from utils.skill_utils import normalize_skill


def build_skill_index(resume):

    index = {}

    def ensure(skill_name):
        skill_name = normalize_skill(skill_name)

        if skill_name not in index:
            index[skill_name] = {
                "mentioned_in_skills": False,
                "projects": [],
                "experience": [],
                "certifications": [],
                "occurrences": 0
            }

        return index[skill_name]

    # ------------------------
    # Skills Section
    # ------------------------

    for skill in resume.skills:

        entry = ensure(skill.name)

        entry["mentioned_in_skills"] = True

        entry["occurrences"] += 1

    # ------------------------
    # Projects
    # ------------------------

    for project in resume.projects:

        for tech in project.technologies:

            entry = ensure(tech)

            entry["projects"].append(project.title)

            entry["occurrences"] += 1

    # ------------------------
    # Experience
    # ------------------------

    for exp in resume.experience:

        for tech in exp.technologies:

            entry = ensure(tech)

            entry["experience"].append(exp.role)

            entry["occurrences"] += 1

    # ------------------------
    # Certifications
    # ------------------------

    for cert in resume.certifications:

        cert_lower = cert.lower()

        for skill in list(index.keys()):

            if skill in cert_lower:

                index[skill]["certifications"].append(cert)

    return index