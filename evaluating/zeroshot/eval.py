import pandas as pd

df = pd.read_csv(r'evaluating\zeroshot\Dreaddit.csv') 

model_cols = [col for col in df.columns if col.startswith('gemini')]

for col in model_cols:
    accuracy = (df['is_depression'] == df[col]).mean()
    print(f"Accuracy for {col}: {accuracy}")


# Accuracy for gemini_15_8b: 0.7034965034965035
# Accuracy for gemini_15: 0.5748251748251748
# Accuracy for gemini_20: 0.5846153846153846
