from fastapi import APIRouter
from app.services.notification_service import add_notification, get_notifications

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/{user_id}")
def add_note(user_id: str, message: str, status: str = "info"):
    add_notification(user_id, message, status)
    return {"message": "Notification added"}

@router.get("/{user_id}")
def fetch_notifications(user_id: str):
    return get_notifications(user_id)