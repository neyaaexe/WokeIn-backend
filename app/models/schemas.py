from pydantic import BaseModel
from typing import List, Optional

class LoginRequest(BaseModel):
    email: str
    password: str
    type: str  # user or company

class LoginResponse(BaseModel):
    token: str
    user_id: str

class ProfileUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    contact: Optional[str]
    sslc: Optional[float]
    hsc: Optional[float]
    ug: Optional[float]
    pg: Optional[float]

class JobCreate(BaseModel):
    title: str
    description: str
    skills: List[str]
    number_of_candidates: int
    deadline: str  # ISO datetime string

class SubmissionResponse(BaseModel):
    status: str
    submission_id: str

class ScoreResponse(BaseModel):
    score: float
    matched_skills: List[str]
    missing_skills: List[str]
    ai_feedback: Optional[str]

class Notification(BaseModel):
    message: str
    status: str
    timestamp: str
    
