import pandas as pd
import os

name = 'SDCNL'
kind = 'val'  # val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)
clean_df = df[['title_clean', 'author_clean', 'selftext_clean', 'is_suicide']]

clean_df['post'] = 'Title: ' + clean_df['title_clean'] + '\nAuthor: ' + \
    clean_df['author_clean'] + '\nPost: ' + clean_df['selftext_clean']

final_df = clean_df[['post', 'is_suicide']]

final_df.to_csv(output_path, index=False)
