bi_zr_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Your task is to classify the given post into 'Yes' or 'No' {}.

**Post for Classification**:
"{}"

**Output Format**:
- Do not provide any additional explanation or commentary. Only output 'Yes' or 'No'.
"""