
from typing import Dict, List
from datetime import datetime

notifications: Dict[str, List[dict]] = {}

def add_notification(user_id: str, message: str, status: str = "info"):
    note = {"message": message, "status": status, "timestamp": datetime.utcnow().isoformat()}
    if user_id not in notifications:
        notifications[user_id] = []
    notifications[user_id].append(note)

def get_notifications(user_id: str):
    return notifications.get(user_id, [])