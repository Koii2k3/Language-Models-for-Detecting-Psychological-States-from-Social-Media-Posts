import pandas as pd
import os

name = 'Loneliness'
kind = 'train'  #  no val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\clean\{}'.format(name)
output_path = r'datasets\clean\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)
df.columns = ['post', 'is_loneliness', 'love_and_affection', 'social_recognition', 'self_esteem_and_belonging', 'others', 'intensity']

df.to_csv(output_path, index=False)
