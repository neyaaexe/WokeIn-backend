from fastapi import APIRouter, UploadFile, File
from app.services.profile_service import get_profile, update_profile

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/{user_id}")
def fetch_profile(user_id: str):
    return get_profile(user_id)

@router.post("/{user_id}")
def update_user_profile(user_id: str, data: dict, resume: UploadFile = File(None)):
    profile = update_profile(user_id, data, resume)
    return profile