from pathlib import Path
import numpy as np
import ollama


BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_FILE = BASE_DIR / "data" / "knowledge_base.txt"


def get_embedding(text):
    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return np.array(response["embeddings"][0], dtype=np.float32)


def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def create_knowledge_index():
    text = KNOWLEDGE_FILE.read_text(encoding="utf-8")

    sections = [
        section.strip()
        for section in text.split("\n\n")
        if section.strip()
    ]

    index = []

    for section in sections:
        embedding = get_embedding(section)

        index.append({
            "text": section,
            "embedding": embedding
        })

    return index


def retrieve_context(query, k=3):
    index = create_knowledge_index()

    query_embedding = get_embedding(query)

    results = []

    for item in index:
        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        results.append({
            "text": item["text"],
            "score": score
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top_results = results[:k]

    context = "\n\n".join(
        item["text"]
        for item in top_results
    )

    return context