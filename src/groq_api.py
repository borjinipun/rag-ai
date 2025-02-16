import requests
from src.config import API_KEY

class GroqAPI:
    @staticmethod
    def query(prompt):
        url = "https://api.groq.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "llama3-8b", "messages": [{"role": "user", "content": prompt}]}
        response = requests.post(url, headers=headers, json=payload)
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
