# feedback_generator.py - format analysis results into human-readable report
def generate_feedback(analysis_results):
    # If analyzer returned parsing error
    if analysis_results.get("error"):
        report = "\n----- Code Review Report -----\n"
        report += "Score: 0/100\n"
        report += "Rating: ❌ Parsing Error\n\n"
        report += "Details:\n"
        report += f"Error: {analysis_results.get('error_message')}\n\n"
        report += "Suggestions:\n"
        for s in analysis_results.get("suggestions", []):
            report += f"• {s}\n"
        report += "------------------------------\n"
        return report

    score = analysis_results.get("score", 0)
    report = "\n----- Code Review Report -----\n"
    report += f"Score: {score}/100\n"

    if score >= 85:
        report += "Rating: ✅ Excellent Code Quality\n"
    elif score >= 65:
        report += "Rating: ⚙️ Good / Needs minor improvement\n"
    elif score >= 40:
        report += "Rating: ⚠️ Fair / Improve structure and clarity\n"
    else:
        report += "Rating: ❌ Poor / Needs major cleanup\n"

    report += "\nDetails:\n"
    report += f"Loops: {analysis_results.get('loops')}\n"
    report += f"Functions: {analysis_results.get('function_defs')}\n"
    report += f"Prints: {analysis_results.get('print_statements')}\n"
    report += f"Comments: {analysis_results.get('comments')}\n"
    report += f"Long lines: {analysis_results.get('long_lines')}\n\n"

    report += "Suggestions:\n"
    for s in analysis_results.get("suggestions", []):
        report += f"• {s}\n"

    report += "------------------------------\n"
    return report
