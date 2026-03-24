from app.services.ranker import rank_sentences

def test_rank_sentences():
    sentences = [
        "Built a machine learning model using Python",
        "I enjoy reading books"
    ]

    job_desc = "Looking for machine learning experience"

    result = rank_sentences(sentences, job_desc, top_k=1)

    assert len(result) == 1
    assert "machine learning" in result[0].lower()
    