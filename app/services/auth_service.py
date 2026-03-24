import uuid
from typing import Optional
from datetime import datetime, timedelta
import jwt

# Dummy in-memory storage (replace with DB)
users = {}
SECRET_KEY = "YOUR_SECRET_KEY"

def register_user(email: str, password: str, user_type: str):
    user_id = str(uuid.uuid4())
    users[user_id] = {"email": email, "password": password, "type": user_type}
    return user_id

def login_user(email: str, password: str, user_type: str) -> Optional[str]:
    for uid, u in users.items():
        if u["email"] == email and u["password"] == password and u["type"] == user_type:
            token = jwt.encode({"user_id": uid, "exp": datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm="HS256")
            return token, uid
    return None, None

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload["user_id"]
        return users.get(user_id)
    except:
        return None