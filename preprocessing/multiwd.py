import pandas as pd
import os

name = 'MultiWD'
kind = 'val'  #  val

data_path = r'datasets\raw\{}\raw_{}.csv'.format(name, kind)
parent_output_path = r'datasets\our\{}'.format(name)
output_path = r'datasets\our\{}\{}.csv'.format(name, kind)

if not os.path.exists(parent_output_path):
    os.makedirs(parent_output_path)

df = pd.read_csv(data_path)
df.columns = ["post", "spiritual", "physical", "intellectual", "social", "vocational", "emotional"]

df.to_csv(output_path, index=False)
