import pandas as pd
import os

name = 'CAMS'
kind = 'train'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

df['post'] = df['text']
df['dep_sui_kind'] = df['category']
df['dep_sui_exp'] = df['explanation']

final_df = df[['post', 'dep_sui_kind', 'dep_sui_exp']]

final_df.to_csv(output_path, index=False)
