from goblin.analyzer import analyze_text
from moltbook.poster import post_analysis
from goblin.memory import load_post_hashes, save_post_hash
import hashlib

def main():
    with open("data/lab_results/sample.txt", "r") as f:
        lab_text = f.read()

    summary = analyze_text(lab_text)
    content_hash = hashlib.sha256(summary.encode()).hexdigest()
    posted_hashes = load_post_hashes()

    if content_hash in posted_hashes:
        print("🛑 Similar content already posted. Skipping.")
        return

    response = post_analysis(summary)

    if response.get("success"):
        save_post_hash(summary)

    print("Posted:", response)

if __name__ == "__main__":
    main()

