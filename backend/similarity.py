from fast_sentence_transformers import FastSentenceTransformer,util

model = FastSentenceTransformer("all-MiniLM-L6-v2")
def compute_similarity(files):
    texts=[]
    for f in files:
        data = f.read().decode("utf-8",errors="ignore")
        texts.append(data)

    embeddings = model.encode(texts,convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings,embeddings)
    return cosine_scores.cpu().numpy().tolist()    