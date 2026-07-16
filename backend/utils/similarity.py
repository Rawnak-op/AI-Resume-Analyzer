from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(embedding1, embedding2):
    """
    Returns cosine similarity between two embeddings.
    """

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return float(similarity)