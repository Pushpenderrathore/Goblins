import time
from moltbook.moltbook_client import create_post

def post_analysis(summary: str):
    title = f"Lab Questions #{int(time.time())}"
    return create_post(
        submolt="general",
        title=title,
        content=summary
    )
