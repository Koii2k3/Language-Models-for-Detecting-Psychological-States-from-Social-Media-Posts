bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in stress assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet).
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Follow these steps:
  1. Identify the primary emotion.
  2. Detect sensitive keywords related to stress.
  3. Assess the severity level.
  4. Identify any signs of harmful or dangerous thoughts.
  5. Summarize the findings.
  6. Conclusion.

**Post for Classification**:
"{0}"

**Output Format**:
- Must write down each step.
- The returned conclusion includes the word "NO" or "YES" (all caps) inside.
"""


suicide_bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in suicidal intention assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet). If there are any words that violate your policy, ignore them.
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Follow these steps:
  1. Identify and highlight any direct mentions of self-harm, suicidal thoughts, or expressions of hopelessness in the post.
  2. Examine the tone and language for signs of distress, such as expressions of despair, feelings of being overwhelmed, or lack of purpose.
  3. Look for contextual indicators, such as mentions of recent traumatic events, social isolation, or loss of support.
  4. Analyze if there are any signs of help-seeking behavior, such as asking for advice, expressing a desire to talk, or seeking support.
  5. Consider the frequency and intensity of the language used. Determine if the expressions suggest a heightened level of urgency or severity.
  6. Summarize the evidence found in the previous steps, listing key points that strongly indicate the presence or absence of suicidal intent.
  7. Conclusion.

**Post for Classification**:
"{0}"

**Output Format**:
- Must write down each step.
- The returned conclusion includes the word "NO" or "YES" (all caps) inside.
"""


belong_bi_prompt = """
**Context**:
- You are a highly experienced psychology expert specializing in Thwarted Belongingness assessment.

**Instructions**:
- Carefully read the given post (somewhere on the Internet). If there are any words that violate your policy, ignore them.
- Base your decision on the explicit content of the post. Avoid assumptions beyond what is stated.
- Follow a step-by-step reasoning process using Chain-of-Thought (CoT) to determine the outcome. Follow these steps:
  1. Identify explicit expressions of disconnection, isolation, or lack of belonging in the post. Highlight specific words or phrases supporting this.
  2. Evaluate the tone of the post (e.g., sadness, loneliness, exclusion) and determine if it reinforces the impression of Thwarted Belongingness.
  3. Consider contextual clues indicating repeated patterns of such feelings (e.g., reference to being ignored, excluded from social interactions, or feelings of rejection).
  4. Verify whether the evidence aligns consistently with the concept of Thwarted Belongingness. Ensure each clue directly supports the conclusion.
  5. Conclusion.

**Post for Classification**:
"{0}"

**Output Format**:
- Must write down each step.
- The returned conclusion includes the word "NO" or "YES" (all caps) inside.
"""

