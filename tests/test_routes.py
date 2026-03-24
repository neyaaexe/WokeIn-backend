from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_parse_route():
    response = client.post(
        "/api/v1/parse",
        files={"resume": ("test.pdf", b"", "application/pdf")}
    )

    assert response.status_code == 200
    assert "sentences" in response.json()


def test_rank_route():
    response = client.post(
        "/api/v1/rank",
        json={
            "sentences": ["Built ML model"],
            "job_description": "Machine learning"
        }
    )

    assert response.status_code == 200
    assert "top_sentences" in response.json()


def test_score_route():
    response = client.post(
        "/api/v1/score",
        json={
            "sentences": ["Built ML model"],
            "job_description": "Machine learning"
        }
    )

    assert response.status_code == 200
    assert "score" in response.json()