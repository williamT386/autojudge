from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset

# ds = load_dataset("Idavidrein/gpqa", "gpqa_diamond", split="train")
ds = load_dataset("jeggers/gpqa_formatted", "diamond", split="train")
df = ds.to_pandas()

search_string = 'of the following'
# consider this dataframe separately
df_with_string = df[df.iloc[:, 0].str.contains(search_string, na=False)]
df_without_string = df[~df.iloc[:, 0].str.contains(search_string, na=False)]
