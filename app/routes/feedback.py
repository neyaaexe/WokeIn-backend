from fastapi import APIRouter
from app.models.schemas import FeedbackRequest
from app.services.ai_feedback import get_ai_feedback

router = APIRouter()

@router.post("/feedback")
def feedback(req: FeedbackRequest):

    ai_response = get_ai_feedback(
        score=req.score,
        matched=req.matched,
        missing_skills=req.missing_skills
    )

    return {
        "feedback": ai_response,
        "decision": "Generated via AI"
    }
    