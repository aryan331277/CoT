from ollama import Client

client = Client()

def call_model(model_name, prompt):
    response = client.generate(model=model_name, prompt=prompt)
    return response['response']
