from sentence_transformers_lite import SentenceTransformersLite,util

model = SentenceTransformersLite("all-MiniLM-L6-v2")
def compute_similarity(files):
    texts=[]
    for f in files:
        data = f.read().decode("utf-8",errors="ignore")
        texts.append(data)

    embeddings = model.encode(texts,convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings,embeddings)
    return cosine_scores.cpu().numpy().tolist()    