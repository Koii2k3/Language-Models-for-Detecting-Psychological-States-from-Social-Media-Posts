import pandas as pd

input_file = 'test.csv' 
output_file = 'prompted_data.csv'

bi_fw_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {condition} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to perform a detailed step-by-step analysis to determine whether the given post shows signs of stress, then classify the post into 'Yes' or 'No' {condition}.

**Enhancement**:
{enhancement}

**Post for Classification**:
"{post}"

**Output Format**:
- Do not provide any additional explanation or commentary. Only output 'Yes' or 'No'.
"""

def create_prompt(post, condition, enhancement):
    return bi_fw_prompt.format(
        condition=condition,
        enhancement=enhancement,
        post=post
    )

df = pd.read_csv(input_file)

condition = "stress detection"
enhancement = "Focus on words that indicate anxiety, overthinking, or overwhelming situations."

df['input'] = df['post'].apply(lambda x: create_prompt(x, condition, enhancement))
df['output'] = df['is_depression'].apply(lambda x: 'Yes' if x == 1 else 'No')

final_df = df[['input', 'output']]
final_df.to_csv(output_file, index=False)

print(f"File mới đã được tạo: {output_file}")