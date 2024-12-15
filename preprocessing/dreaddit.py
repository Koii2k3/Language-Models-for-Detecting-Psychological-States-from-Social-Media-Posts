import pandas as pd
import os

name = 'Dreaddit'
kind = 'val'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\our\{}'.format(name)
output_path = r'datasets\our\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)

clean_df = df[['subreddit', 'text', 'label']]

clean_df['post'] = 'Topic: ' + \
    clean_df['subreddit'] + '\nPost: ' + clean_df['text']
clean_df['is_depression'] = df['label']

final_df = clean_df[['post', 'is_depression']]

final_df.to_csv(output_path, index=False)
