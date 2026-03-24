from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight, fast

def rank_sentences(resume_sentences, job_description):
    """
    Rank candidate resume sentences against job description using embeddings
    """
    if not resume_sentences:
        return [], []

    job_embedding = model.encode(job_description, convert_to_tensor=True)
    sentence_embeddings = model.encode(resume_sentences, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(sentence_embeddings, job_embedding)
    scores = cosine_scores.squeeze().tolist()

    ranked = sorted(zip(resume_sentences, scores), key=lambda x: x[1], reverse=True)
    ranked_sentences = [r[0] for r in ranked]
    ranked_scores = [r[1] for r in ranked]
    return ranked_sentences, ranked_scores