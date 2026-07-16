# AI Resume Intelligence Platform

## Overview

AI Resume Intelligence Platform is a full-stack web application that analyzes resumes against job descriptions, computes ATS compatibility scores, identifies missing skills, and generates AI-powered resume improvements using Large Language Models.

The application combines semantic similarity, skill matching, ATS scoring, and resume rewriting to help users optimize their resumes for specific job roles.

---

## Features

- Resume parsing from PDF
- ATS compatibility analysis
- Semantic similarity matching
- Multi-factor ATS scoring
- Required and missing skill detection
- Resume quality assessment
- ATS score breakdown
- AI-powered resume recommendations
- AI-powered resume rewriting
- Interactive dashboard

---

## Technology Stack

### Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- Framer Motion
- React Markdown

### Backend

- FastAPI
- Python
- Pydantic

### AI & Machine Learning

- Google Gemini API
- LangChain
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn

### Data Processing

- PyMuPDF
- NumPy

---

## ATS Evaluation Criteria

The ATS score is computed using multiple weighted factors.

| Category | Description |
|----------|-------------|
| Semantic Match | Measures resume relevance to the job description |
| Skills Match | Evaluates required and optional skills |
| Experience | Assesses relevant experience |
| Projects | Measures project relevance |
| Keywords | Evaluates important ATS keywords |
| Resume Sections | Checks completeness of essential sections |
| Resume Quality | Evaluates overall resume quality |

---

## System Workflow

```text
Resume PDF
    │
    ▼
PDF Text Extraction
    │
    ▼
Resume Information Extraction
    │
    ▼
Job Description Analysis
    │
    ▼
Sentence Transformer Embeddings
    │
    ▼
Semantic Similarity Computation
    │
    ▼
ATS Scoring Engine
    │
    ├────────► Skill Matching
    ├────────► Recommendations
    └────────► Resume Rewriting
```

---

## Project Structure

```text
AI-Resume-Intelligence-Platform

│── backend
│   ├── ats
│   ├── chains
│   ├── models
│   ├── services
│   ├── utils
│   ├── parser.py
│   ├── embeddings.py
│   ├── app.py
│   └── requirements.txt
│
│── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── services
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>

cd AI-Resume-Intelligence-Platform
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## Environment Variables

Create a `.env` file inside the backend directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## API Endpoints

### Resume Analysis

```
POST /match
```

Returns:

- ATS Score
- ATS Breakdown
- Matched Skills
- Missing Skills
- Recommendations

### Resume Rewrite

```
POST /rewrite
```

Returns:

- AI-generated resume rewrite

---

## Future Enhancements

- Resume PDF export
- Cover letter generation
- Interview question generation
- Multiple resume templates
- Recruiter dashboard
- Authentication
- Docker support
- Cloud deployment

---

## License

This project is released under the MIT License.