from app.services.job_service import create_job, list_jobs, get_job

def test_jobs():
    job_id, job = create_job("AI Engineer", "Build models", ["Python", "ML"], 5, "2026-05-01", "company1")
    assert job["title"] == "AI Engineer"
    all_jobs = list_jobs()
    assert any(j["title"] == "AI Engineer" for j in all_jobs)
    fetched = get_job(job_id)
    assert fetched["number_of_candidates"] == 5