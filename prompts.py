THINKER_PROMPT = """
Solve the following question step by step.
Show your full Chain-of-Thought reasoning clearly.

Question: {question}
"""

CRITIC_PROMPT = """
You are a reasoning analyst.
Extract all logical/mathematical claims from the following Chain-of-Thought.

Chain-of-Thought: {reasoning}

Return them as a list:
1. ...
2. ...
"""
