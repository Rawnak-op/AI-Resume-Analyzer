"""
resume_model.py

Structured Resume model used throughout the application.
"""

from typing import List
from pydantic import BaseModel, Field


# ------------------------------------
# Skill
# ------------------------------------

class Skill(BaseModel):
    """
    Represents one skill extracted from the resume.
    """

    name: str = Field(
        description="Skill name"
    )

    source: str = Field(
        description="Where the skill was found. Example: Skills, Projects, Experience"
    )

    confidence: float = Field(
        default=1.0,
        description="Confidence that this skill exists"
    )


# ------------------------------------
# Project
# ------------------------------------

class Project(BaseModel):

    title: str = Field(
        description="Project title"
    )

    description: str = Field(
        description="Short project description"
    )

    technologies: List[str] = Field(
        default_factory=list,
        description="Technologies used"
    )


# ------------------------------------
# Experience
# ------------------------------------

class Experience(BaseModel):

    company: str

    role: str

    duration: str

    start_date: str = ""

    end_date: str = ""

    employment_type: str = ""

    description: str = ""

    technologies: list[str] = Field(default_factory=list)

# ------------------------------------
# Education
# ------------------------------------

class Education(BaseModel):

    degree: str

    institution: str

    year: str


# ------------------------------------
# Resume
# ------------------------------------

class Resume(BaseModel):

    name: str

    email: str

    phone: str

    summary: str = ""

    skills: List[Skill] = Field(default_factory=list)

    projects: List[Project] = Field(default_factory=list)

    experience: List[Experience] = Field(default_factory=list)

    education: List[Education] = Field(default_factory=list)

    certifications: List[str] = Field(default_factory=list)

    achievements: List[str] = Field(default_factory=list)