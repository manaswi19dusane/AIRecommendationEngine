
from airec.infrastructure.model_store import ModelStore

class Trainer:

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def train(self, data_source, **kwargs):

        items = data_source.load_items()

        model = self.algorithm.fit(items, **kwargs)

        return model

    def save_model(self, model, path):

        ModelStore.save(model, path)
