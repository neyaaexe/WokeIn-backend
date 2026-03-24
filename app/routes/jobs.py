
from fastapi import APIRouter
from app.services.job_service import create_job, list_jobs, get_job

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/")
def add_job(title: str, description: str, skills: list, num_candidates: int, deadline: str, company_id: str):
    job_id, job = create_job(title, description, skills, num_candidates, deadline, company_id)
    return {"job_id": job_id, "job": job}

@router.get("/")
def all_jobs():
    return list_jobs()

@router.get("/{job_id}")
def job_detail(job_id: str):
    job = get_job(job_id)
    if job:
        return job
    return {"error": "Job not found"}