import requests

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

def query_hf_model(prompt, hf_token):
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.4,
            "max_new_tokens": 512,
            "do_sample": True
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()[0]["generated_text"]
    except requests.exceptions.RequestException as e:
        return f"[Error] {str(e)}"
