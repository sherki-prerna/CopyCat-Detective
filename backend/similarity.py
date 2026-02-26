from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def clean_text(t):
    return " ".join(t.lower().split())

def compute_similarity(files):
    texts = []

    for f in files:
        try:
            content = f.read().decode("utf-8", errors="ignore")
        except:
            content = ""
        texts.append(clean_text(content))

    if len(texts) < 2:
        return {"error": "Upload at least 2 files"}

    # Generate embeddings for ALL files
    embeddings = model.encode(texts)

    # Normalize for consistent cosine similarity
    embeddings = normalize(embeddings)

    # Compute full NxN similarity matrix
    matrix = cosine_similarity(embeddings)

    # Replace any NaN/inf with 0
    matrix = np.nan_to_num(matrix, nan=0.0, posinf=1.0, neginf=0.0)

    # Round for stable values like 1.0, 0.89
    matrix = np.round(matrix, 4)

    return {
        "matrix": matrix.tolist()
    }
