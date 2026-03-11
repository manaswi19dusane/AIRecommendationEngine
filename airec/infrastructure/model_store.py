
import pickle

class ModelStore:

    @staticmethod
    def save(model, path):

        with open(path, "wb") as f:
            pickle.dump(model, f)

    @staticmethod
    def load(path):

        with open(path, "rb") as f:
            return pickle.load(f)
