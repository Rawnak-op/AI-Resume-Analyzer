"""
semantic.py

Calculates semantic similarity score using Sentence Transformer embeddings.
The similarity value should already be cosine similarity between
resume embedding and job description embedding.
"""


def semantic_score(similarity: float) -> dict:
    """
    Converts cosine similarity into a percentage.

    Parameters
    ----------
    similarity : float
        Cosine similarity between 0 and 1.

    Returns
    -------
    dict
        {
            "semantic_score": 84.21
        }
    """

    similarity = max(0.0, min(1.0, similarity))

    score = round(similarity * 100, 2)

    return {
        "semantic_score": score
    }
