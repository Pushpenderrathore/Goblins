from goblin.analyzer import analyze_text
from moltbook.poster import post_analysis
from goblin.memory import load_replied_comments, mark_replied
import hashlib
import time
from pathlib import Path


DATA_FILE = Path("data/lab_results/sample.txt")


def main():
    if not DATA_FILE.exists():
        print("❌ Data file not found:", DATA_FILE)
        return

    lab_text = DATA_FILE.read_text()

    summary = analyze_text(lab_text)

    # Use content hash as unique post ID
    content_hash = hashlib.sha256(summary.encode()).hexdigest()

    replied_hashes = load_replied_comments()

    if content_hash in replied_hashes:
        print("🛑 Similar content already posted. Skipping.")
        return

    response = post_analysis(summary)

    if response.get("success"):
        mark_replied(content_hash)
        print("✅ Posted successfully.")
    else:
        print("❌ Post failed.")

    print("Response:", response)


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print("🔥 Runtime error:", e)

        time.sleep(1800)  # 30 minutes
