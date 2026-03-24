from fastapi import APIRouter, UploadFile, File
from app.services.submission_service import submissions
from app.services.score_service import compute_submission_score
from app.services.job_service import get_job

router = APIRouter(prefix="/scores", tags=["scores"])

@router.post("/{submission_id}")
def score_submission(submission_id: str, use_ai_feedback: bool = True):
    submission = submissions.get(submission_id)
    if not submission:
        return {"error": "Submission not found"}

    job = get_job(submission["job_id"])
    score_data = compute_submission_score(
        submission,
        job_description=job["description"],
        job_keywords=job["skills"],
        company_name="CompanyName",
        use_ai_feedback=use_ai_feedback
    )
    return score_data