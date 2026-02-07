import json
from pathlib import Path
import tempfile
import os

# Always resolve relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "replied_comments.json"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_replied_comments():
    if not LOG_FILE.exists():
        return set()

    try:
        data = json.loads(LOG_FILE.read_text())
        return set(data.get("replied_comment_ids", []))
    except Exception:
        # Corrupted file fallback
        return set()


def mark_replied(comment_id: str):
    replied = load_replied_comments()
    replied.add(comment_id)

    # Atomic write (prevents corruption)
    with tempfile.NamedTemporaryFile(
        "w",
        delete=False,
        dir=LOG_FILE.parent
    ) as tmp:
        json.dump({"replied_comment_ids": list(replied)}, tmp, indent=2)
        temp_name = tmp.name

    os.replace(temp_name, LOG_FILE)
