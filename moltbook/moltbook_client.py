import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.moltbook.com/api/v1"
API_KEY = os.getenv("MOLTBOOK_API_KEY")

if not API_KEY:
    raise RuntimeError("MOLTBOOK_API_KEY not set")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_post(submolt: str, title: str, content: str):
    payload = {
        "submolt": submolt,
        "title": title,
        "content": content
    }
    r = requests.post(f"{BASE_URL}/posts", json=payload, headers=HEADERS, timeout=10)
    return r.json()
