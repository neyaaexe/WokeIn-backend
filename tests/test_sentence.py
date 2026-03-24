from app.services.sentence import get_sentences

def test_sentence_split():
    text = "I built a model. It works well."
    sentences = get_sentences(text)

    assert len(sentences) == 2
    assert "built a model" in sentences[0].lower()
    