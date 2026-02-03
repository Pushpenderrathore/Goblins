from goblin.analyzer import analyze_text
from moltbook.poster import post_analysis

def main():
    # Example lab data (replace with real lab file reading)
    lab_text = """
    Nmap scan shows open ports 80 and 443.
    Test environment: DVWA lab.
    """

    summary = analyze_text(lab_text)
    response = post_analysis(summary)

    print("Posted to Moltbook:", response)

if __name__ == "__main__":
    main()
