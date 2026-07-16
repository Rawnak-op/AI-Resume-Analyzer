"""
config.py

Loads environment variables and application configuration.
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# ===========================
# Gemini
# ===========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ===========================
# Embedding Model
# ===========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===========================
# ATS Weights
# (Must sum to 100)
# ===========================

ATS_WEIGHTS = {

    "semantic": 20,

    "required_skills": 20,

    "preferred_skills": 10,

    "keywords": 10,

    "experience": 10,

    "sections": 10,

    "achievements": 10,

    "action_verbs": 5,

    "formatting": 5
}