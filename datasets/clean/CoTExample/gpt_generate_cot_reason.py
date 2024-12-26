from tqdm import tqdm
import pandas as pd
from openai import OpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import generate_cot_example

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
gen_ex_model = "gpt_4o_mini"

data_name = "Irf_belong"
data_path = r'datasets/clean/{}/train.csv'.format(data_name)
data = pd.read_csv(data_path)

output_file = f'datasets/clean/CoTExample/{data_name}/train.csv'

if os.path.exists(output_file):
    data = pd.read_csv(output_file)
    if gen_ex_model not in data.keys():
        data[gen_ex_model] = ""
        data.to_csv(output_file, index=False)
        data = pd.read_csv(output_file)
else:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    data[gen_ex_model] = ""
    data.to_csv(output_file, index=False)
    data = pd.read_csv(output_file)

data[gen_ex_model] = data[gen_ex_model].astype(object)

for index, row in tqdm(data.iterrows(), total=data.shape[0]):
    if pd.isna(row[gen_ex_model]):
        filled_prompt = generate_cot_example.gen_cot_prompt.format(
            'Thwarted Belongingness', row['post'])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": filled_prompt}],
        )

        response = response.choices[0].message.content
        data.loc[index, gen_ex_model] = response.replace('"', '').strip()
        data.to_csv(output_file, index=False)
