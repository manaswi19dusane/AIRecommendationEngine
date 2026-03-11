
from airec.infrastructure.model_store import ModelStore

class Recommender:

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def load_model(self, path):
        self.algorithm.model = ModelStore.load(path)

    def recommend(self, item_id, top_n=5):
        return self.algorithm.recommend(item_id, top_n)
