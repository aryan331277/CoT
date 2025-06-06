THINKER_PROMPT = """
Solve the following question step by step.
Show your full Chain-of-Thought reasoning clearly.

Question: {question}
"""

CRITIC_PROMPT = """
You are a reasoning analyst.
Extract only the *logical* and *mathematical* claims from the following chain-of-thought reasoning.
Return them as a JSON list of strings, no commentary, no prefix.

Chain-of-Thought:
{reasoning}

Return:
[
  "claim1",
  "claim2",
  ...
]
"""
