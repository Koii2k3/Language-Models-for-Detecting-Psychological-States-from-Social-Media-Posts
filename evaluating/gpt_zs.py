from tqdm import tqdm
import pandas as pd
from openai import OpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompting import zero_shot

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
eval_model = "gpt_4o_mini"

data_name = "Dreaddit"
data_path = r'datasets/clean/{}/val.csv'.format(data_name)
data = pd.read_csv(data_path)

output_file = f'evaluating/zeroshot/{data_name}.csv'

if os.path.exists(output_file):
    data = pd.read_csv(output_file)
    if eval_model not in data.keys():
        data[eval_model] = ""
        data.to_csv(output_file, index=False)
        data = pd.read_csv(output_file)
else:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    data[eval_model] = ""
    data.to_csv(output_file, index=False)
    data = pd.read_csv(output_file)

data[eval_model] = data[eval_model].astype(object)

for index, row in tqdm(data.iterrows(), total=data.shape[0]):
    if pd.isna(row[eval_model]):
        filled_prompt = zero_shot.bi_zr_prompt.format(
            'depression', 'depression', row['post'])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": filled_prompt}],
        )

        response = response.choices[0].message.content
        data.loc[index, eval_model] = response.replace('"', '').strip()
        data.to_csv(output_file, index=False)
        exit()
