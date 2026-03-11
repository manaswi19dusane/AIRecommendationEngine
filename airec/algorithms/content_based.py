
from airec.utils.text_vectorizer import SimpleVectorizer
from airec.utils.similarity import cosine_similarity
from airec.domain.models import RecommendationModel

class ContentBased:

    def __init__(self):
        self.model = None

    def fit(self, df, id_col="item_id", text_col="content"):

        texts = df[text_col].fillna("").tolist()

        vectorizer = SimpleVectorizer()

        matrix = vectorizer.fit_transform(texts)

        similarity = cosine_similarity(matrix)

        item_index = {df[id_col].iloc[i]: i for i in range(len(df))}

        self.model = RecommendationModel(similarity, item_index)

        return self.model

    def recommend(self, item_id, top_n=5):

        idx = self.model.item_index[item_id]

        scores = list(enumerate(self.model.similarity_matrix[idx]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        scores = scores[1: top_n + 1]

        return [i[0] for i in scores]
