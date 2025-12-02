from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(files):
    texts = []

    for f in files:
        try:
            content = f.read().decode("utf-8", errors="ignore")
        except:
            content = ""
        texts.append(content)

    if len(texts) < 2:
        return {"error": "Need at least two files"}

    embeddings = model.encode(texts)
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    return {"similarity": float(score)}
