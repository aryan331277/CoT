import requests

MODEL_NAME = "tiiuae/falcon-7b-instruct"
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

def query_hf_model(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 256,
            "temperature": 0.4,
            "do_sample": True
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list):
            return result[0]['generated_text']
        elif isinstance(result, dict) and 'error' in result:
            return f"[Error] {result['error']}"
        else:
            return str(result)
    except Exception as e:
        return f"[Error] {str(e)}"
