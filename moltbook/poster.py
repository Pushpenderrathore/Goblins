from moltbook.moltbook_client import create_post

def post_analysis(summary: str):
    title = "Lab Insight: Common Recon Mistakes"
    return create_post(
        submolt="general",
        title=title,
        content=summary
    )
