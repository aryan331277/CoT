import requests

def query_hf_model(prompt, hf_token):
    MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

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
        resp_json = response.json()

        if isinstance(resp_json, list) and 'generated_text' in resp_json[0]:
            return resp_json[0]['generated_text']
        elif isinstance(resp_json, dict) and 'generated_text' in resp_json:
            return resp_json['generated_text']
        elif "estimated_time" in resp_json:
            return "[Info] Model is warming up. Please retry in a few seconds."
        else:
            return "[Error] Unexpected response format."
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return "[Error] Invalid or missing Hugging Face token."
        elif response.status_code == 403:
            return "[Error] You don't have access to this model."
        elif response.status_code == 503:
            return "[Error] Model is currently overloaded or not ready."
        else:
            return f"[Error] HTTP {response.status_code}: {response.text}"
    except Exception as e:
        return f"[Error] {str(e)}"
