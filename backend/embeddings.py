import torch
torch.set_num_threads(1)
from sentence_transformers import SentenceTransformer

from cache import get_cached_embedding, set_cached_embedding

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """
    Returns a 384-D embedding vector for the given text.

    Cache flow:
      1. Check Redis for a pre-computed embedding (TTL: 6h).
      2. On cache miss, run the SentenceTransformer model.
      3. Store the result in Redis before returning.
    """

    # --- Layer 1: Cache HIT ---
    cached = get_cached_embedding(text)
    if cached is not None:
        return cached

    # --- Cache MISS: run the model ---
    embedding = model.encode(text)

    # --- Store in cache ---
    set_cached_embedding(text, embedding)

    return embedding
