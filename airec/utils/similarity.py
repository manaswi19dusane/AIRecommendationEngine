from sklearn.metrics.pairwise import cosine_similarity as sk_cosine

def cosine_similarity(matrix):
    return sk_cosine(matrix)   # works with both sparse and dense
    norm = np.linalg.norm(matrix, axis=1)
    similarity = np.dot(matrix, matrix.T) / (norm[:, None] * norm[None, :])
    similarity[np.isnan(similarity)] = 0
    return similarity
