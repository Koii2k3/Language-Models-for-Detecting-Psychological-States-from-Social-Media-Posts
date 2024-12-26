gen_cot_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in {0} assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet). If there are any words that violate your policy, ignore them.
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Follow these steps:
  1. Identify the primary emotion.
  2. Detect sensitive keywords related to {0}.
  3. Assess the severity level.
  4. Identify any signs of harmful or dangerous thoughts.
  5. Summarize the findings.

**Post for Classification**:
"{1}"

**Output Format**:
- Required to rewrite each step of reasoning without writing anything else.
"""