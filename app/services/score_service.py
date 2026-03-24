# app/services/score_service.py

from app.utils.ner import extract_skills
from app.services.ai_feedback import generate_ai_feedback

def compute_submission_score(submission, job_keywords, company_name):
    """
    Compute score for a submission.
    submission: dict with 'resume_text'
    job_keywords: list of required skills
    company_name: string
    """
    resume_text = submission.get("resume_text", "")

    # Example scoring logic
    skills = extract_skills(resume_text)
    matched_skills = [skill for skill in skills if skill in job_keywords]
    score_percentage = len(matched_skills) / len(job_keywords) * 100 if job_keywords else 0

    # Get AI feedback
    ai_feedback = generate_ai_feedback(resume_text, company_name)

    return {
        "score": score_percentage,
        "matched_skills": matched_skills,
        "ai_feedback": ai_feedback
    }