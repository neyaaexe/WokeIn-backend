# tests/test_scorer.py
from unittest.mock import patch
from app.services.score_service import compute_submission_score

def test_scoring_with_ai():
    submission = {"resume_text": "Python, ML, AWS", "job_id": "job1"}
    job_keywords = ["Python", "ML", "AWS", "Docker"]
    company_name = "TechCorp"

    with patch("app.services.ai_feedback.generate_ai_feedback", return_value="Mock AI feedback"):
        score = compute_submission_score(submission, job_keywords, company_name)
        assert isinstance(score, dict)
        assert "ai_feedback" in score
