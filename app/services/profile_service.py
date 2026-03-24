from typing import Dict
from fastapi import UploadFile
from app.utils.parser import parse_resume

profiles: Dict[str, dict] = {}

def get_profile(user_id: str):
    return profiles.get(user_id, {})

def update_profile(user_id: str, data: dict, resume: UploadFile = None):
    if resume:
        resume_text = parse_resume(resume)
        data["resume_text"] = resume_text
        data["resume_filename"] = resume.filename
    profiles[user_id] = data
    return profiles[user_id]