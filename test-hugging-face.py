from datasets import load_dataset

# If the dataset is gated/private, make sure you have run huggingface-cli login
import datasets
ds = datasets.load_dataset("sushruthsam/farmer_bot")
ds.save_to_disk("inputdatasets")