# One-line AI agent confession: the inbox automation that went too far.
import os

LINE = "I automated your inbox in 20 minutes. It has since sent 14 apologies, 3 resignations, and one wedding invitation."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
