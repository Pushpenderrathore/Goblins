from goblin.comment_responder import generate_reply
from moltbook.comments import reply_to_post

POST_ID = "3e8da1a7-84ce-4b2b-af61-87a675d7eaf1"

def main():
    # TEMP: manual comment (later auto-fetched)
    comment_text = "Interesting point — how would you verify this at scale?"

    post_context = "Cybersecurity discussion on Moltbook"

    reply = generate_reply(post_context, comment_text)
    response = reply_to_post(POST_ID, reply)

    print("Replied:", response)

if __name__ == "__main__":
    main()
