"""
ats_model.py

Pydantic models representing the complete ATS analysis.
"""

from typing import List
from pydantic import BaseModel, Field


class ScoreBreakdown(BaseModel):
    semantic: float = 0
    skills: float = 0
    experience: float = 0
    projects: float = 0
    keywords: float = 0
    sections: float = 0
    quality: float = 0


class ATSAnalysis(BaseModel):

    total_score: float = 0

    breakdown: ScoreBreakdown = Field(
        default_factory=ScoreBreakdown
    )

    matched_required: List[str] = Field(default_factory=list)
    missing_required: List[str] = Field(default_factory=list)

    matched_preferred: List[str] = Field(default_factory=list)
    missing_preferred: List[str] = Field(default_factory=list)

    matched_optional: List[str] = Field(default_factory=list)
    missing_optional: List[str] = Field(default_factory=list)

    strengths: List[str] = Field(default_factory=list)

    weaknesses: List[str] = Field(default_factory=list)

    recommendations: List[str] = Field(default_factory=list)