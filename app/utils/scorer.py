from .ner import extract_skills
from .ranker import rank_sentences

def compute_score(resume_text, job_description, job_keywords=None):
    # Extract candidate skills from resume
    candidate_skills = extract_skills(resume_text)

    # Combine job description + job keywords
    if job_keywords is None:
        job_keywords = []
    combined_job_text = job_description + " " + " ".join(job_keywords)

    # Rank sentences (optional, not strictly needed for scoring)
    ranked_sentences, _ = rank_sentences(resume_text.split("\n"), combined_job_text)

    # Compute match and missing skills
    matched = [skill for skill in candidate_skills if skill.lower() in combined_job_text.lower()]
    missing = [skill for skill in job_keywords if skill not in matched]

    # Simple score calculation
    total_skills = len(job_keywords) if job_keywords else 1
    score = len(matched)/total_skills*100
    score = round(score, 2)

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
    }