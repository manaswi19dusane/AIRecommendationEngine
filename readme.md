
# AI Recommendation Engine V2

Features:
- Content Based Recommendation
- Collaborative Filtering
- Hybrid Recommendation
- CSV Data Source
- MySQL Data Source
- Trainable Models
- Clean Architecture

Example:

from airec import Trainer
from airec.algorithms.content_based import ContentBased
from airec.data_sources.csv_source import CSVSource

source = CSVSource("books.csv")
trainer = Trainer(ContentBased())

model = trainer.train(source)
