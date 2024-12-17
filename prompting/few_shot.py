bi_fw_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to classify the given post into 'Yes' or 'No' {}.

**Enhancement**:
{}
**Post for Classification**:
"{}"

**Output Format**:
- Do not provide any additional explanation or commentary or punctuation. Only output is Yes or No.
"""


mul_fw_prompt = """
**Context**:
- You are a psychologist specializing in assessing the severity of {}.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to classify the given post into ONE of the predefined categories of {} below: 
  {}

**Enhancement**:
{}
**Post for Classification**:
"{}"

**Output Format**:
- Do not provide any additional explanation or commentary or punctuation. Only ONE of the predefined categories.
"""
