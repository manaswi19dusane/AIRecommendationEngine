import os
import pickle
import pandas as pd
from airec.data_sources.csv_source import CSVSource
from airec.algorithms.content_based import ContentBased

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "Books.csv")

data_source = CSVSource(csv_path)
df = data_source.load_items()

df = df.head(1000)  # remove this limit after fixing sparse matrix

df = df.rename(columns={
    "ISBN":        "item_id",
    "Book-Author": "content",
})

algorithm = ContentBased()
model = algorithm.fit(df)

# ── Save model to pkl ──────────────────────────────────────────────────────
pkl_path = os.path.join(base_dir, "model.pkl")
with open(pkl_path, "wb") as f:
    pickle.dump(algorithm, f)

print(f"✅ Model trained and saved to {pkl_path}")