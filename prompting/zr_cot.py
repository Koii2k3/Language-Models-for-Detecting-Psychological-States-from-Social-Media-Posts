bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {0} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to perform a detailed step-by-step analysis to determine whether the given post shows signs of stress, then classify the post into 'Yes' or 'No' {0}.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Do not write out the intermediate reasoning steps, only the final conclusion. Follow these steps:
  1. Identify the primary emotion.
  2. Detect sensitive keywords related to {0}.
  3. Assess the severity level.
  4. Identify any signs of harmful or dangerous thoughts.
  5. Summarize the findings.

**Post for Classification**:
"{1}"

**Output Format**:
- Do not provide any additional explanation or commentary or punctuation. Only output is Yes or No.
"""


mul_prompt = """
**Context**:
- You are a psychologist specializing in assessing the severity of {}.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to perform a detailed step-by-step analysis to determine whether the given post shows signs of stress, then classify the post into ONE of the predefined categories of {} below: 
  {}

**Post for Classification**:
"{}"

**Output Format**:
- Do not provide any additional explanation or commentary or punctuation. Only ONE of the predefined categories.
"""
