"""
analyzer.py

Main ATS Engine
"""

from models.ats_model import ATSAnalysis

from ats.skill_score import calculate_skill_score
from ats.experience_score import calculate_experience_score
from ats.project_score import calculate_project_score
from ats.keyword_score import calculate_keyword_score
from ats.section_score import calculate_section_score
from ats.quality_score import calculate_quality_score


class ATSAnalyzer:

    def __init__(
        self,
        resume,
        job,
        semantic_similarity
    ):

        self.resume = resume
        self.job = job
        self.semantic_similarity = semantic_similarity

    def analyze(self):

        analysis = ATSAnalysis()

        # ==========================================
        # Semantic Similarity (20 Marks)
        # ==========================================

        semantic_score = self.semantic_similarity * 100

        analysis.breakdown.semantic = round(
            semantic_score * 0.20,
            2
        )

        # ==========================================
        # Skill Score (25 Marks)
        # ==========================================

        skill = calculate_skill_score(
            self.resume,
            self.job
        )

        analysis.breakdown.skills = round(
            skill["score"] * 0.25,
            2
        )

        analysis.matched_required = skill["matched_required"]
        analysis.missing_required = skill["missing_required"]

        analysis.matched_preferred = skill["matched_preferred"]
        analysis.missing_preferred = skill["missing_preferred"]

        analysis.matched_optional = skill["matched_optional"]
        analysis.missing_optional = skill["missing_optional"]

        # ==========================================
        # Experience (15 Marks)
        # ==========================================

        experience = calculate_experience_score(
            self.resume,
            self.job
        )

        analysis.breakdown.experience = round(
            experience["score"] * 0.15,
            2
        )

        # ==========================================
        # Projects (10 Marks)
        # ==========================================

        project = calculate_project_score(
            self.resume,
            self.job
        )

        analysis.breakdown.projects = round(
            project["score"] * 0.10,
            2
        )

        # ==========================================
        # Keywords (10 Marks)
        # ==========================================

        keyword = calculate_keyword_score(
            self.resume,
            self.job
        )

        analysis.breakdown.keywords = round(
            keyword["score"] * 0.10,
            2
        )

        # ==========================================
        # Resume Sections (10 Marks)
        # ==========================================

        section = calculate_section_score(
            self.resume
        )

        analysis.breakdown.sections = round(
            section["score"] * 0.10,
            2
        )

        # ==========================================
        # Resume Quality (10 Marks)
        # ==========================================

        quality = calculate_quality_score(
            self.resume
        )

        analysis.breakdown.quality = round(
            quality["score"] * 0.10,
            2
        )

        # ==========================================
        # Strengths
        # ==========================================

        if skill["required_score"] >= 85:
            analysis.strengths.append(
                "Excellent coverage of required technical skills."
            )

        if experience["score"] >= 100:
            analysis.strengths.append(
                "Experience satisfies the job requirement."
            )

        if project["score"] >= 80:
            analysis.strengths.append(
                "Projects closely align with the target role."
            )

        if keyword["score"] >= 80:
            analysis.strengths.append(
                "Strong keyword coverage."
            )

        if quality["score"] >= 80:
            analysis.strengths.append(
                "Resume contains strong action verbs and measurable achievements."
            )

        if semantic_score >= 85:
            analysis.strengths.append(
                "Resume is highly relevant to the job description."
            )

        # ==========================================
        # Weaknesses
        # ==========================================

        if skill["required_score"] < 70:
            analysis.weaknesses.append(
                "Several required technical skills are missing."
            )

        if experience["score"] < 100:
            analysis.weaknesses.append(
                "Relevant experience could be stronger."
            )

        if project["score"] < 50:
            analysis.weaknesses.append(
                "Projects are not closely aligned with the job."
            )

        if keyword["score"] < 60:
            analysis.weaknesses.append(
                "Important job keywords are missing."
            )

        if quality["score"] < 60:
            analysis.weaknesses.append(
                "Resume quality can be improved using stronger action verbs and quantified achievements."
            )

        if semantic_score < 70:
            analysis.weaknesses.append(
                "Resume content is not sufficiently aligned with the job description."
            )

        # ==========================================
        # Recommendations
        # ==========================================

        for missing in skill["missing_required"]:
            analysis.recommendations.append(
                f"Add or demonstrate '{missing}' through projects or experience."
            )

        for missing in skill["missing_preferred"]:
            analysis.recommendations.append(
                f"Consider adding experience with '{missing}'."
            )

        if experience["score"] < 100:
            analysis.recommendations.append(
                "Gain more relevant work or internship experience."
            )

        if project["score"] < 50:
            analysis.recommendations.append(
                "Include projects that better match this role."
            )

        if keyword["score"] < 60:
            analysis.recommendations.append(
                "Include more job-specific keywords naturally throughout your resume."
            )

        if quality["score"] < 60:
            analysis.recommendations.append(
                "Use action verbs and quantify achievements wherever possible."
            )

        if semantic_score < 70:
            analysis.recommendations.append(
                "Tailor your resume to better match the job description."
            )

        # ==========================================
        # Final ATS Score
        # ==========================================

        analysis.total_score = round(

            analysis.breakdown.semantic +

            analysis.breakdown.skills +

            analysis.breakdown.experience +

            analysis.breakdown.projects +

            analysis.breakdown.keywords +

            analysis.breakdown.sections +

            analysis.breakdown.quality,

            2

        )

        return analysis