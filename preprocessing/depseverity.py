import pandas as pd
import os

name = 'DepSeverity'
kind = 'train'  #  no val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\our\{}'.format(name)
output_path = r'datasets\our\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

df['post'] = df['text']
df['depression_kind'] = df['label']

final_df = df[['post', 'depression_kind']]

final_df.to_csv(output_path, index=False)
