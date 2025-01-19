bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {0} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to classify the given post into 'Yes' or 'No' {0}.

**Enhancement**:
{1}
**Post for Classification**:
"{2}"

**Output Format**:
- Do not provide any additional explanation or commentary or punctuation. Only output is Yes or No.
"""
