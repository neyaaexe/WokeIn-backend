from fastapi import APIRouter, HTTPException
from app.services.auth_service import register_user, login_user, verify_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(email: str, password: str, user_type: str):
    user_id = register_user(email, password, user_type)
    return {"user_id": user_id, "message": "User registered successfully"}

@router.post("/login")
def login(email: str, password: str, user_type: str):
    token, user_id = login_user(email, password, user_type)
    if token:
        return {"token": token, "user_id": user_id}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/verify")
def verify(token: str):
    user = verify_token(token)
    if user:
        return {"user": user}
    raise HTTPException(status_code=401, detail="Invalid token")