from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def cross_score(sentences, job_description):
    if not sentences:
        return []

    pairs = [(s, job_description) for s in sentences]
    scores = model.predict(pairs)

    return list(zip(sentences, scores))


def compute_score(scored_sentences):
    if not scored_sentences:
        return 0

    values = [score for _, score in scored_sentences]

    max_score = max(values)
    avg_score = sum(values) / len(values)

    final = (0.6 * max_score) + (0.4 * avg_score)
    return round(final * 100, 2)
