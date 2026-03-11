
from abc import ABC, abstractmethod

class IAlgorithm(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def recommend(self, item_id, top_n):
        pass
