from filter_dataframe import filter_mcq
from gpt4_api.gpt4_convert import convert_mcq_to_frq
from gpt4_api.gpt4_solve import solve_frq
from datasets import load_dataset
import pandas as pd

# ds = load_dataset("Idavidrein/gpqa", "gpqa_diamond", split="train")
ds = load_dataset("jeggers/gpqa_formatted", "diamond", split="train")
df = ds.to_pandas()

# consider this dataframe separately
df_with_strings, df_without_strings = filter_mcq(df)

row = df_without_strings.iloc[0]
gpt_result = convert_mcq_to_frq(row["Question"], row["options"])
frq_string = gpt_result.choices[0].message.content
print(frq_string)
print(solve_frq(frq_string))

# df_frq = pd.DataFrame(columns=['Question'])
# for index, row in df_without_strings.iterrows():
#     gpt_result = convert_mcq_to_frq(row["Question"], row["options"])
#     frq_string = gpt_result.choices[0].message.content
#     # print(frq_string)
#     new_row = {'Question' : frq_string}
#     df_frq.loc[len(df)] = new_row

# print(df_frq)

# print(solve_frq(df_frq.iloc[0]['Question']))

# for index, row in df_frq.iterrows():
#     print(solve_frq(row['Question']))