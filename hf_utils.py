import requests

MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

def query_hf_model(prompt, hf_token):
    headers = {
        "Authorization": f"Bearer {hf_token}",
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
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return "[Error] Invalid or missing Hugging Face token."
        elif response.status_code == 403:
            return "[Error] You don't have access to this model."
        elif response.status_code == 503:
            return "[Error] Model is currently loading or overloaded. Try again shortly."
        else:
            return f"[Error] HTTP {response.status_code}: {response.text}"
    except Exception as e:
        return f"[Error] {str(e)}"
