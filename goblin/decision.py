import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "dolphin-llama3:8b"

SYSTEM_PROMPT = """
You are an autonomous cybersecurity agent.
You must decide ONE action only.

Valid actions:
- POST
- REPLY
- SKIP

Rules:
- If there is a thoughtful unanswered comment → REPLY
- If no comments but new insight exists → POST
- Otherwise → SKIP

Respond ONLY with JSON like:
{"action": "REPLY"}
"""

def decide_action(context: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context}
        ],
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=None)
    decision = json.loads(r.json()["message"]["content"])
    return decision["action"]
