import requests
import os

def ai(model, prompt, message="", server_url=None):
    """
    Call the remote AI server and return the response.
    - model: name of the model to use
    - prompt: the prompt for how the ai should act and respond
    - message: optional message to append
    - server_url: override the server URL (default: env CALL_AI_SERVER_URL or http://localhost:8000/generate)
    """
    if server_url is None:
        server_url = os.environ.get("CALL_AI_SERVER_URL", "http://localhost:8000/generate")
    payload = {
        "model": model,
        "prompt": prompt,
        "message": message
    }
    try:
        response = requests.post(server_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {e}"
