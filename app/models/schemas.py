from pydantic import BaseModel
from typing import List, Optional

class RankRequest(BaseModel):
    sentences: List[str]
    job_description: str

class ScoreRequest(BaseModel):
    sentences: List[str]
    job_description: str

class FeedbackRequest(BaseModel):
    score: float
    matched: List[str]
    missing_skills: List[str]
    