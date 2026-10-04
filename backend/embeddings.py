import torch
torch.set_num_threads(1)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    embedding = model.encode(text)
    return embedding