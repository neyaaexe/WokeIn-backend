import uuid
from typing import List, Dict

jobs: Dict[str, dict] = {}

def create_job(title: str, description: str, skills: List[str], num_candidates: int, deadline: str, company_id: str):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "title": title,
        "description": description,
        "skills": skills,
        "number_of_candidates": num_candidates,
        "deadline": deadline,
        "company_id": company_id
    }
    return job_id, jobs[job_id]

def list_jobs():
    return list(jobs.values())

def get_job(job_id: str):
    return jobs.get(job_id)