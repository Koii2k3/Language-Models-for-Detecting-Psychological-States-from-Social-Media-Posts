import pandas as pd
import os

name = 'Irf'
kind = 'test'  #  val, test

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output1_path = r'datasets\clean\{}\{}1.csv'.format(name, kind)
output2_path = r'datasets\clean\{}\{}2.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

df['post'] = df['text']
df['is_belong'] = df['belong'].map({0: 'No', 1: 'Yes'})
df['is_burden'] = df['burden'].map({0: 'No', 1: 'Yes'})

first_dataset = df[['post', 'is_belong']]
second_dataset = df[['post', 'is_burden']]

first_dataset.to_csv(output1_path, index=False)
second_dataset.to_csv(output2_path, index=False)



