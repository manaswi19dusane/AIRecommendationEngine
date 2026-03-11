
from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def load_items(self):
        pass

    @abstractmethod
    def load_interactions(self):
        pass
