from app.services.scorer import cross_score, compute_score

def test_cross_score():
    sentences = ["Built ML model"]
    job_desc = "Machine learning experience"

    scored = cross_score(sentences, job_desc)
    scored = [(sentence, float(score)) for sentence, score in scored]

    assert len(scored) == 1
    assert isinstance(scored[0][1], float)


def test_compute_score():
    scored = [("test", 0.8), ("test2", 0.6)]
    score = compute_score(scored)
    score = float(score)
    assert score > 0
    assert score <= 100
