
import pandas as pd
import mysql.connector
from airec.data_sources.base_source import DataSource

class MySQLSource(DataSource):

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def load_items(self):
        query = "SELECT * FROM items"
        return pd.read_sql(query, self.connection)

    def load_interactions(self):
        query = "SELECT * FROM interactions"
        return pd.read_sql(query, self.connection)
