from utils import call_model
from prompts import THINKER_PROMPT, CRITIC_PROMPT

def thinker(question):
    prompt = THINKER_PROMPT.format(question=question)
    return call_model("mixtral", prompt)

def critic(reasoning):
    prompt = CRITIC_PROMPT.format(reasoning=reasoning)
    return call_model("mistral", prompt)
