from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_sentences(sentences, job_description, top_k=10):
    if not sentences:
        return []

    sent_emb = model.encode(sentences, convert_to_tensor=True)
    job_emb = model.encode(job_description, convert_to_tensor=True)

    scores = util.cos_sim(sent_emb, job_emb)[0]

    top_k = min(top_k, len(sentences))
    top_results = scores.topk(k=top_k)

    return [sentences[i] for i in top_results.indices]
