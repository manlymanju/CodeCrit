# main.py - entry point for CodeCrit (CLI)
from analyzer import analyze_code
from feedback_generator import generate_feedback
import os

def main():
    print("!!!!! CodeCrit — An Intelligent Python Code Reviewer !!!!!")
    file_path = input("Enter path of Python file to analyze: ").strip()

    if not os.path.exists(file_path):
        print("XXXXX File not found. Please check the path and try again.....")
        return

    print("\nAnalyzing your code... please wait.\n")

    analysis_results = analyze_code(file_path)
    feedback = generate_feedback(analysis_results)

    print(feedback)

    os.makedirs("results", exist_ok=True)
    report_path = os.path.join("results", "report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(feedback)

    print(f"✅ Report saved to: {report_path}")

if __name__ == "__main__":
    main()
