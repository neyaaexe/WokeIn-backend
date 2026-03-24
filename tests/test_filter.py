from app.services.filter import fast_filter, skill_filter

def test_fast_filter():
    sentences = [
        "Short",
        "This is a valid sentence with enough words"
    ]

    result = fast_filter(sentences)
    assert len(result) == 1


def test_skill_filter():
    sentences = [
        "I worked on Python and ML",
        "I like music"
    ]

    skills = ["python", "ml"]

    result = skill_filter(sentences, skills)

    assert len(result) == 1
    assert "python" in result[0].lower()
    