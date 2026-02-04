import time
from goblin.decision import decide_action
from goblin.comment_responder import generate_reply
from goblin.memory import load_replied_comments, mark_replied
from moltbook.comments import reply_to_post

POST_ID = "3e8da1a7-84ce-4b2b-af61-87a675d7eaf1"

# TEMP: manual comment input (replace with API fetch later)
COMMENTS = [
    {"id": "c1", "text": "This sounds risky. How would you secure it?"},
    {"id": "c2", "text": "Interesting philosophy behind this."}
]

def main():
    replied = load_replied_comments()

    context = f"""
Recent comments:
{COMMENTS}

Already replied:
{list(replied)}
"""

    action = decide_action(context)
    print("🧠 Decision:", action)

    if action == "REPLY":
        for c in COMMENTS:
            if c["id"] in replied:
                continue

            reply = generate_reply("Moltbook discussion", c["text"])
            reply_to_post(POST_ID, reply)
            mark_replied(c["id"])

            print(f"💬 Replied to {c['id']}")
            break

    elif action == "POST":
        print("📝 Posting logic goes here (reuse main.py)")

    else:
        print("😴 Nothing to do")

if __name__ == "__main__":
    main()
