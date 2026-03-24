# tests/test_profile.py
import pytest
from unittest.mock import patch

# IMPORT the function from your service
from app.services.profile_service import update_profile

def test_update_profile():
    data = {"name": "Alice", "email": "alice@example.com"}

    # Patch parse_resume to avoid actual PDF parsing
    with patch("app.services.profile_service.parse_resume", return_value="Dummy resume text"):
        profile = update_profile("user1", data, resume=None)
        assert profile["name"] == "Alice"
        assert profile["email"] == "alice@example.com"