
class RecommendationModel:
    def __init__(self, similarity_matrix, item_index):
        self.similarity_matrix = similarity_matrix
        self.item_index = item_index
