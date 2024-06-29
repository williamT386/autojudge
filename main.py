from gpt4_api.gpt4_convert import convert_mcq_to_frq
from datasets import load_dataset

# ds = load_dataset("Idavidrein/gpqa", "gpqa_diamond", split="train")
ds = load_dataset("jeggers/gpqa_formatted", "diamond", split="train")
df = ds.to_pandas()

search_string = 'of the following'
# consider this dataframe separately
df_with_string = df[df.iloc[:, 0].str.contains(search_string, na=False)]
df_without_string = df[~df.iloc[:, 0].str.contains(search_string, na=False)]

row = df_without_string.iloc[4]
gpt_result = convert_mcq_to_frq(row["Question"], row["options"])
print(gpt_result.choices[0].message)