import pandas as pd

df = pd.read_csv(r'evaluating\fewshot1\Dreaddit.csv') 

model_cols = [col for col in df.columns if col.startswith('gemini')]

for col in model_cols:
    accuracy = (df['is_depression'] == df[col]).mean()
    print(f"Accuracy for {col}: {accuracy}")

# Accuracy for gemini_15_8b: 0.7174825174825175
# Accuracy for gemini_15: 0.6223776223776224
# Accuracy for gemini_20: 0.7062937062937062
