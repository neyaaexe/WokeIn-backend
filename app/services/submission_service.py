import uuid
from typing import List, Dict
from fastapi import UploadFile
from app.utils.parser import parse_resume

submissions: Dict[str, dict] = {}

def submit_resume(user_id: str, job_id: str, resume: UploadFile):
    sub_id = str(uuid.uuid4())
    resume_text = parse_resume(resume)
    submissions[sub_id] = {
        "user_id": user_id,
        "job_id": job_id,
        "resume_filename": resume.filename,
        "resume_text": resume_text
    }
    return sub_id, submissions[sub_id]

def get_submissions(job_id: str):
    return [s for s in submissions.values() if s["job_id"] == job_id]