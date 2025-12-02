from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import functools

# Ensures model loads only once
@functools.lru_cache()
def load_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def compute_similarity(files):
    texts = []

    for f in files:
        content = f.read().decode("utf-8", errors="ignore")
        texts.append(content)

    if len(texts) < 2:
        return {"error": "At least 2 files required"}

    model = load_model()
    embeddings = model.encode(texts)

    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    return {
        "similarity": float(score),
        "percentage": round(float(score) * 100, 2)
    }
