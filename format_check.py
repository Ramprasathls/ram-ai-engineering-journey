from pathlib import Path

from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")
Path("data").mkdir(exist_ok=True)
dataset.to_csv("data/imdb_train.csv")
dataset.to_parquet("data/imdb_train.parquet")
