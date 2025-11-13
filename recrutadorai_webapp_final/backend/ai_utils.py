import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util

# Modelo semântico multilíngue (português incluso)
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")

def clean_text(text):
    """Remove símbolos, espaços extras e deixa tudo minúsculo."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-ZÀ-ÿ0-9 ]', '', text)
    return text.lower().strip()

def semantic_similarity(job_desc, candidates):
    """Calcula similaridade semântica via embeddings."""
    job_emb = model.encode(job_desc, convert_to_tensor=True)
    cand_embs = model.encode([c["text"] for c in candidates], convert_to_tensor=True)
    sims = util.pytorch_cos_sim(job_emb, cand_embs)[0].cpu().numpy()
    return sims

def tfidf_similarity(job_desc, candidates):
    """Calcula similaridade tradicional (TF-IDF)."""
    texts = [job_desc] + [c["text"] for c in candidates]
    vectorizer = TfidfVectorizer(stop_words=None)
    tfidf = vectorizer.fit_transform(texts)
    job_vec = tfidf[0:1]
    cand_vecs = tfidf[1:]
    sims = (cand_vecs @ job_vec.T).toarray().flatten()
    return sims

def analyze_candidates(job_description, candidates):
    """Combina análise semântica + TF-IDF + pesos inteligentes."""
    job_description = clean_text(job_description)
    for c in candidates:
        c["text"] = clean_text(c["text"])

    sem_sim = semantic_similarity(job_description, candidates)
    tfidf_sim = tfidf_similarity(job_description, candidates)

    combined = 0.75 * sem_sim + 0.25 * tfidf_sim
    for i, c in enumerate(candidates):
        c["score"] = float(np.clip(combined[i], 0, 1))

    ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)
    return ranked
