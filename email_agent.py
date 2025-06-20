import requests

TOGETHER_API_KEY = "cdbba383fd8c3095f64b182c7e9a227190848e453523d9796bc238c5de5a29c9"  # paste your key here

def smart_email_reply(email_text, sender_name=""):
    prompt = f"""
You are a polite and professional email assistant.

Received Email:
\"\"\"
{email_text}
\"\"\"

Write a formal reply to {sender_name}:
"""

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # You can switch this to other models
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.5,
        "stop": ["User:", "Assistant:"]
    }

    response = requests.post("https://api.together.ai/v1/completions", json=body, headers=headers)

    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return f"❌ Error: {response.status_code} - {response.json()}"
