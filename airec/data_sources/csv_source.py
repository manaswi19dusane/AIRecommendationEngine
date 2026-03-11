
import pandas as pd
from airec.data_sources.base_source import DataSource

class CSVSource(DataSource):

    def __init__(self, item_path, interaction_path=None):
        self.item_path = item_path
        self.interaction_path = interaction_path

    def load_items(self):
        return pd.read_csv(self.item_path)

    def load_interactions(self):
        if self.interaction_path:
            return pd.read_csv(self.interaction_path)
        return None
