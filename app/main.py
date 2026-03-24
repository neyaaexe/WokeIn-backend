from fastapi import FastAPI
from app.routes import analyze, parse, rank, score, feedback

app = FastAPI(title="AI Hiring System")

app.include_router(analyze.router, prefix="/api/v1")
app.include_router(parse.router, prefix="/api/v1")
app.include_router(rank.router, prefix="/api/v1")
app.include_router(score.router, prefix="/api/v1")
app.include_router(feedback.router, prefix="/api/v1")
