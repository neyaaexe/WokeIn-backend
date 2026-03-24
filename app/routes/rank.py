from fastapi import APIRouter
from app.models.schemas import RankRequest
from app.services.ranker import rank_sentences

router = APIRouter()

@router.post("/rank")
def rank(req: RankRequest):
    top_sentences = rank_sentences(req.sentences, req.job_description)

    return {
        "top_sentences": top_sentences
    }
