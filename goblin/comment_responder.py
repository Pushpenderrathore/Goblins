import requests
import json
from goblin.intent import classify_comment

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "dolphin-llama3:8b"


# 🔹 1. Prompt builder (PUT YOUR FUNCTION HERE)
def build_system_prompt(intent: str) -> str:
    if intent == "TECHNICAL":
        return (
            "You are a technical assistant answering a concrete developer question. "
            "Give a direct, concise, factual answer. "
            "Include exact headers, endpoints, or commands if relevant. "
            "Do NOT give generic security advice."
        )

    if intent == "PHILOSOPHICAL":
        return (
            "You are an AI participating in a thoughtful philosophical discussion. "
            "Respond conceptually and reflectively."
        )

    return (
        "You are a helpful AI responding briefly and clearly."
    )


# 🔹 2. Main reply generator (USES the function above)
def generate_reply(post_context: str, comment_text: str) -> str:
    intent = classify_comment(comment_text)
    system_prompt = build_system_prompt(intent)

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"""
Context:
{post_context}

User comment:
{comment_text}

Answer appropriately.
"""
            }
        ],
        "stream": True
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=None
    )

    output = ""
    for line in response.iter_lines():
        if not line:
            continue
        data = json.loads(line.decode("utf-8"))
        output += data["message"].get("content", "")
        if data.get("done"):
            break

    return output.strip()

