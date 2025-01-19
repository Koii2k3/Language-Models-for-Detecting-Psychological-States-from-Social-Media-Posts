import os
import sys
import time
import string
import google.generativeai as genai
import pandas as pd
from tqdm import tqdm
import numpy as np
import random
from dotenv import load_dotenv
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompting import few_shot
load_dotenv()

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Evaluate Gemini model with few-shot learning.")
parser.add_argument("--key_number", type=int, default=1,
                    help="The key number to use (GEMINI_API_KEY{key_number}).")
parser.add_argument("--dataset_name", type=str,
                    default="SDCNL", help="The dataset name.")
parser.add_argument("--eval_type", type=str, default="val",
                    help="The subset evaluating on")
parser.add_argument("--task_name", type=str,
                    default="suicide", help="The dataset column task name")
parser.add_argument("--task_desc", type=str,
                    default="suicide", help="The full name of the task")
parser.add_argument("--model_codename", type=str,
                    default="gemini-2.0-flash-exp", help="The model codename to use.")
args = parser.parse_args()

seed_value = 42
np.random.seed(seed_value)
random.seed(seed_value)

GEMINI_API_KEY = os.getenv(f"GEMINI_API_KEY{args.key_number}")
print(GEMINI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model_codename = args.model_codename
model = genai.GenerativeModel(
    model_name=model_codename,
    generation_config=generation_config,
)
eval_model = "".join(
    char for char in model_codename if char not in string.punctuation).replace(" ", "_")

# Load and prepare data
data_name = args.dataset_name
data_path = r'datasets/clean/{}/{}.csv'.format(data_name, args.eval_type)
data = pd.read_csv(data_path)  # Load validation data
output_file = f'evaluating/fs_{eval_model}/{data_name}.csv'

example_data_path = r'datasets/clean/{}/train.csv'.format(data_name)
example_data = pd.read_csv(example_data_path)  # Load training data

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

data[eval_model] = data[eval_model].astype(
    object)  # Ensure eval column is type object

# Iterate through each row and perform model inference
for index, row in tqdm(data.iterrows(), total=data.shape[0], desc=f'{eval_model}_{data_name}'):
    if pd.isna(row[eval_model]):
        np.random.seed(index)  # Set seed for consistent sampling
        samples_per_label = example_data.groupby(f'is_{args.task_name}').sample(
            n=1, random_state=index).reset_index(drop=True)
        few_examples = ""
        for idx, sample_row in samples_per_label.iterrows():
            few_examples += example_template.format(
                idx + 1, sample_row['post'], sample_row[f'is_{args.task_name}'])

        filled_prompt = few_shot.bi_prompt.format(
            args.task_desc, few_examples, row['post'])

        response = model.generate_content(filled_prompt)  # Generate content

        data.loc[index, eval_model] = response.text.replace('"', '').strip()

        data.to_csv(output_file, index=False)  # Save to CSV after each update
        time.sleep(5) if eval_model != "gemini20flashexp" else time.sleep(6.5)
