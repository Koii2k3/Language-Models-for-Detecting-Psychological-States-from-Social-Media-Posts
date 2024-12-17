import os
import sys
import time
import google.generativeai as genai
import pandas as pd
from tqdm import tqdm
import numpy as np
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompting import few_shot

seed_value = 42
np.random.seed(seed_value)
random.seed(seed_value)

# Configure API and model
genai.configure(api_key=os.getenv('GEMINI_KEY1')) # Set API key
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # gemini-1.5-flash-8b (gemini-1.5-flash-8b-001), gemini-1.5-flash (gemini-1.5-flash-002), gemini-1.5-pro, gemini-2.0-flash-exp (gemini-2.0-flash-exp)
    generation_config=generation_config,
)
eval_model = 'gemini_15' # Model name for evaluation

# Load and prepare data
data_name = "Dreaddit"
data_path = r'datasets/clean/{}/val.csv'.format(data_name)
data = pd.read_csv(data_path) # Load validation data
output_file = f'evaluating/{eval_model}/{data_name}.csv'

example_data_path = r'datasets/clean/{}/train.csv'.format(data_name)
example_data = pd.read_csv(example_data_path) # Load training data

# Initialize output CSV with a new evaluation column
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


example_template = """  Example {0}:
  Post {0}: "{1}"
  Label {0}: {2}
  
"""

data[eval_model] = data[eval_model].astype(object) # Ensure eval column is type object

# Iterate through each row and perform model inference
for index, row in tqdm(data.iterrows(), total=data.shape[0], desc=f'{eval_model}_{data_name}'):
    if pd.isna(row[eval_model]):
        np.random.seed(index) # Set seed for consistent sampling
        samples_per_label = example_data.groupby('is_depression').sample(n=1, random_state=index).reset_index(drop=True)
        few_examples = ""
        for idx, sample_row in samples_per_label.iterrows():
            few_examples += example_template.format(idx + 1, sample_row['post'], sample_row['is_depression'])
        
        filled_prompt = few_shot.bi_fw_prompt.format(
            'depression', 'depression', few_examples, row['post'])
        
        response = model.generate_content(filled_prompt) # Generate content

        data.loc[index, eval_model] = response.text.replace('"', '').strip()
        
        data.to_csv(output_file, index=False) # Save to CSV after each update
        time.sleep(6) # Sleep for rate limiting
