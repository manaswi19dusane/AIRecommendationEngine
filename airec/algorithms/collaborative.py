
import pandas as pd
from airec.utils.similarity import cosine_similarity
from airec.domain.models import RecommendationModel

class CollaborativeFiltering:

    def __init__(self):
        self.model = None
        self.user_item_matrix = None

    def fit(self, df):

        matrix = df.pivot_table(
            index="user_id",
            columns="item_id",
            values="rating"
        ).fillna(0)

        similarity = cosine_similarity(matrix.values)

        item_index = {i: idx for idx, i in enumerate(matrix.columns)}

        self.user_item_matrix = matrix

        self.model = RecommendationModel(similarity, item_index)

        return self.model

    def recommend(self, user_id, top_n=5):

        user_row = self.user_item_matrix.loc[user_id]

        unseen = user_row[user_row == 0]

        return unseen.index[:top_n].tolist()
