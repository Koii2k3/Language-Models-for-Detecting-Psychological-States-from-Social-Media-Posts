import pandas as pd
import os

name = 'SAD'
kind = 'train'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

clean_df = df[['sentence', 'is_stressor', 'original_label']]

clean_df['post'] = clean_df['sentence']
clean_df['is_stress'] =  clean_df['is_stressor'].map({0: 'No', 1: 'Yes'})
clean_df['stress_kind'] = df['original_label']

final_df = clean_df[['post', 'is_stress', 'stress_kind']]

final_df.to_csv(output_path, index=False)
