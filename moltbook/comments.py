import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://www.moltbook.com/api/v1"
API_KEY = os.getenv("MOLTBOOK_API_KEY")

if not API_KEY:
    raise RuntimeError("MOLTBOOK_API_KEY not set")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def reply_to_post(post_id: str, text: str):
    """
    Reply to a Moltbook post (comment).
    """
    url = f"{API_BASE}/posts/{post_id}/comments"
    payload = {"content": text}

    r = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()
