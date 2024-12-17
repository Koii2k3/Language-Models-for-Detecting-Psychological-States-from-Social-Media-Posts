import os
import sys
import time
import google.generativeai as genai
import pandas as pd
from tqdm import tqdm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompting import zero_shot


genai.configure(api_key=os.getenv('GEMINI_KEY1'))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",  # gemini-1.5-flash-8b (gemini-1.5-flash-8b-001), gemini-1.5-flash (gemini-1.5-flash-002), gemini-1.5-pro, gemini-2.0-flash-exp (gemini-2.0-flash-exp)
    generation_config=generation_config,
)
eval_model = 'gemini_15_8b'

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

        response = model.generate_content(filled_prompt)

        data.loc[index, eval_model] = response.text.replace('"', '').strip()
        data.to_csv(output_file, index=False)
        time.sleep(7)
        