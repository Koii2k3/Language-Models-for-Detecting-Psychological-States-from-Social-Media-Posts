import pandas as pd
import os

name = 'Irf'
kind = 'test'  #  val, test

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

df['post'] = df['text']
df['is_belong'] = df['belong'].map({0: 'No', 1: 'Yes'})
df['is_burden'] = df['burden'].map({0: 'No', 1: 'Yes'})

final_df = df[['post', 'is_belong', 'belong_exp', 'is_burden', 'burden_exp']]

final_df.to_csv(output_path, index=False)
