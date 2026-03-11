
from airec import Trainer
from airec.algorithms.content_based import ContentBased
from airec.data_sources.mysql_source import MySQLSource

source = MySQLSource(
    host="localhost",
    user="root",
    password="1234",
    database="recommendation"
)

trainer = Trainer(ContentBased())

model = trainer.train(
    source,
    id_col="item_id",
    text_col="description"
)
