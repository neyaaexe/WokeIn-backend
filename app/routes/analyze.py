from app.services.ai_feedback import get_ai_feedback

from fastapi import APIRouter, UploadFile, File, Form
import json

from app.services.parser import extract_pdf
from app.services.sentence import get_sentences
from app.services.filter import fast_filter, skill_filter
from app.services.ranker import rank_sentences
from app.services.scorer import cross_score, compute_score

router = APIRouter()

@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    job_keywords: str = Form(...),
    options: str = Form(...)
):
    job_keywords = json.loads(job_keywords)
    options = json.loads(options)

    # Step 1: Extract text
    text = extract_pdf(resume.file)

    # Step 2: Sentence split
    sentences = get_sentences(text)

    # Step 3: Filtering
    sentences = fast_filter(sentences)
    sentences = skill_filter(sentences, job_keywords)

    # Step 4: Ranking
    top_sentences = rank_sentences(sentences, job_description)

    # Step 5: Scoring
    scored = cross_score(top_sentences, job_description)
    final_score = compute_score(scored)

    # Step 6: Missing skills (basic)
    missing = [
        skill for skill in job_keywords
        if not any(skill in s.lower() for s, _ in scored)
    ]

    ai_output = None

    if options.get("use_ai_feedback", False):
        ai_output = get_ai_feedback(
            score=final_score,
            matched=[s for s, _ in scored],
            missing_skills=missing
        )

    return {
        "score": final_score,
        "matched": [
            {"sentence": s, "score": float(sc)}
            for s, sc in scored
        ],
        "missing_skills": missing,
        "decision": "Strong Hire" if final_score > 80 else "Consider",
        "ai_feedback": {
            "enabled": options.get("use_ai_feedback", False),
            "content": ai_output
        }
    }