from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")
split = dataset["train"].train_test_split(test_size=0.2, seed=42)

train_ds = split["train"]
val_ds = split["test"]
test_ds = dataset["test"]

print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")
