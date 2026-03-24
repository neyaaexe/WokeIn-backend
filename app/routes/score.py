from fastapi import APIRouter
from app.models.schemas import ScoreRequest
from app.services.scorer import cross_score, compute_score

router = APIRouter()

@router.post("/score")
def score(req: ScoreRequest):
    scored = cross_score(req.sentences, req.job_description)
    final_score = compute_score(scored)
    final_score = float(final_score) 
    return {
        "score": final_score,
        "sentence_scores": [
            {"sentence": s, "score": float(sc)}
            for s, sc in scored
        ]
    }
