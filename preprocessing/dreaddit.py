import pandas as pd
import os

name = 'Dreaddit'
kind = 'val'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

clean_df = df[['text', 'label']]

clean_df['post'] = clean_df['text']
clean_df['is_depression'] = df['label'].map({0: 'No', 1: 'Yes'})

final_df = clean_df[['post', 'is_depression']]

final_df.to_csv(output_path, index=False)
