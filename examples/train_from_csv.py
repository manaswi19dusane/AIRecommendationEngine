
from airec import Trainer
from airec.algorithms.content_based import ContentBased
from airec.data_sources.csv_source import CSVSource

source = CSVSource("books.csv")

trainer = Trainer(ContentBased())

model = trainer.train(
    source,
    id_col="item_id",
    text_col="content"
)

trainer.save_model(model, "book_model.pkl")
