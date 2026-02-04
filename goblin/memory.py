import json
from pathlib import Path

LOG_FILE = Path("logs/replied_comments.json")

def load_replied_comments():
    if not LOG_FILE.exists():
        return set()
    data = json.loads(LOG_FILE.read_text())
    return set(data.get("replied_comment_ids", []))

def mark_replied(comment_id: str):
    replied = load_replied_comments()
    replied.add(comment_id)
    LOG_FILE.write_text(json.dumps({
        "replied_comment_ids": list(replied)
    }, indent=2))
