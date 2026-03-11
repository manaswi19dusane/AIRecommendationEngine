
import numpy as np

def cosine_similarity(matrix):
    norm = np.linalg.norm(matrix, axis=1)
    similarity = np.dot(matrix, matrix.T) / (norm[:, None] * norm[None, :])
    similarity[np.isnan(similarity)] = 0
    return similarity
