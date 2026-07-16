"""
job_model.py

Pydantic model representing a Job Description.
"""

from typing import List
from pydantic import BaseModel, Field


class Technologies(BaseModel):

    languages: List[str] = Field(default_factory=list)

    frameworks: List[str] = Field(default_factory=list)

    databases: List[str] = Field(default_factory=list)

    cloud: List[str] = Field(default_factory=list)

    tools: List[str] = Field(default_factory=list)


class Job(BaseModel):

    role: str

    role_confidence: float

    required_skills: List[str]

    preferred_skills: List[str]

    optional_skills: List[str]

    minimum_experience: str

    technologies: Technologies

    keywords: List[str]

    summary: str