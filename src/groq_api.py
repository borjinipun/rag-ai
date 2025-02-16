import requests
from src.config import API_KEY

class GroqAPI:
    @staticmethod
    def query(prompt):
        url = "https://api.groq.com/openai/v1/chat/completions"  # Corrected URL
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}]}
        
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        
        print("Groq API Response:", response_json)  # Debugging line
        
        return response_json.get("choices", [{}])[0].get("message", {}).get("content", "")
