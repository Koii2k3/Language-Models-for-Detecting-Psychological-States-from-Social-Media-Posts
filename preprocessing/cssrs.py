import pandas as pd
import os

name = 'CSSRS'
kind = 'train'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\our\{}'.format(name)
output_path = r'datasets\our\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

clean_df = df[['Post', 'Label']]

clean_df['post'] = clean_df['Post']
clean_df['suicide_kind'] = df['Label']

final_df = clean_df[['post', 'suicide_kind']]

final_df.to_csv(output_path, index=False)
