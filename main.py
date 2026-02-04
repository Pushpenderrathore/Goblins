from goblin.analyzer import analyze_text
from moltbook.poster import post_analysis

def main():
    with open("data/lab_results/sample.txt", "r") as f:
        lab_text = f.read()

    summary = analyze_text(lab_text)
    response = post_analysis(summary)

    print("Posted:", response)

if __name__ == "__main__":
    main()

