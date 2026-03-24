# tests/test_submission.py
import pytest
from io import BytesIO
from unittest.mock import patch
from fastapi import UploadFile
from app.services.submission_service import submit_resume

def test_submit_resume():
    fake_file = UploadFile(filename="resume.pdf", file=BytesIO(b"%PDF-1.4 fake content"))

    # Patch parse_resume to avoid PDF parsing
    with patch("app.services.submission_service.parse_resume", return_value="Dummy resume text"):
        sub_id, sub = submit_resume("user1", "job1", resume=fake_file)
        assert sub_id is not None
        assert sub["user_id"] == "user1"
        assert sub["job_id"] == "job1"
        assert sub["resume_filename"] == "resume.pdf"