from jina_embeddings import Embeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load tiny, fast, lightweight model
embedder = Embeddings(model_name="jina-embedding-tiny-en")

def compute_similarity(files):
    texts = []

    # Read uploaded files as text
    for file in files:
        content = file.read().decode("utf-8", errors="ignore")
        texts.append(content)

    # Need at least two files
    if len(texts) < 2:
        return {"error": "Upload at least 2 files"}

    # Get embeddings for all texts
    embeddings = embedder.embed(texts)

    # Cosine similarity between first two files
    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return {"similarity": float(score)}
