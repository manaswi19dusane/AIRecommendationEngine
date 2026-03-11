
class HybridRecommender:

    def __init__(self, content_model, collaborative_model):
        self.content_model = content_model
        self.collaborative_model = collaborative_model

    def recommend(self, item_id, user_id, top_n=5):

        content_rec = self.content_model.recommend(item_id, top_n)
        collab_rec = self.collaborative_model.recommend(user_id, top_n)

        combined = list(set(content_rec + collab_rec))

        return combined[:top_n]
