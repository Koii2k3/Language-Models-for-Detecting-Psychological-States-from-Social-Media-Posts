bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {0} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Follow these steps:
  1. Identify the primary emotion.
  2. Detect sensitive keywords related to {0}.
  3. Assess the severity level.
  4. Identify any signs of harmful or dangerous thoughts.
  5. Summarize the findings.
  6. Conclusion.

**Post for Classification**:
"{1}"

**Output Format**:
- Must write down each step.
- The returned conclusion includes the word "NO" or "YES" (all caps) inside.
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
- Must write down each step.
- The returned conclusion includes the word "No" or "Yes" inside.
"""
