from fastapi import APIRouter, UploadFile, File
from app.services.submission_service import submit_resume, get_submissions

router = APIRouter(prefix="/submissions", tags=["submissions"])

@router.post("/{user_id}/{job_id}")
def submit(user_id: str, job_id: str, resume: UploadFile = File(...)):
    sub_id, sub_data = submit_resume(user_id, job_id, resume)
    return {"submission_id": sub_id, "submission": sub_data}

@router.get("/{job_id}")
def submissions_for_job(job_id: str):
    return get_submissions(job_id)