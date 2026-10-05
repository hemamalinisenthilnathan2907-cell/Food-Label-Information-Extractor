from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(text: str):
    """
    Split OCR text into lines and create embeddings.
    """
    sentences = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not sentences:
        return [], None

    embeddings = model.encode(
        sentences,
        convert_to_numpy=True
    )

    return sentences, embeddings
