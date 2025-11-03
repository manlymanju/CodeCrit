# analyzer.py - core static analysis using AST and simple heuristics
import ast

def analyze_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        code = "".join(lines)

    # Parse code into AST (Abstract Syntax Tree)
    try:
        tree = ast.parse(code)
    except Exception as e:
        # If parsing fails (SyntaxError/IndentationError), report it
        return {
            "error": True,
            "error_message": str(e),
            "score": 0,
            "suggestions": [f"Parsing error: {e}"]
        }

    results = {
        "loops": 0,
        "print_statements": 0,
        "function_defs": 0,
        "comments": 0,
        "long_lines": 0,
        "unused_vars": [],
        "score": 100,
        "suggestions": []
    }

    # Structural checks via AST
    for node in ast.walk(tree):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            results["loops"] += 1
        if isinstance(node, ast.FunctionDef):
            results["function_defs"] += 1
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                results["print_statements"] += 1
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    results["unused_vars"].append(target.id)

    # Readability: long lines (>80 chars)
    for line in lines:
        if len(line.rstrip("\n")) > 80:
            results["long_lines"] += 1

    # Comments count (simple heuristic: lines starting with #)
    for line in lines:
        if line.strip().startswith("#"):
            results["comments"] += 1

    # Unused variable check (basic heuristic)
    used_names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    results["unused_vars"] = [v for v in results["unused_vars"] if v not in used_names]

    # Scoring (simple rule-based deductions)
    if results["long_lines"] > 0:
        results["score"] -= results["long_lines"] * 2
        results["suggestions"].append("Some lines exceed 80 characters — consider breaking them for readability.")
    if results["comments"] == 0:
        results["score"] -= 10
        results["suggestions"].append("No comments detected — add inline comments or docstrings.")
    if results["function_defs"] == 0:
        results["score"] -= 5
        results["suggestions"].append("No functions defined — consider organizing code into functions.")
    if results["print_statements"] > 5:
        results["score"] -= 5
        results["suggestions"].append("Too many print statements — remove debugging prints from production code.")
    if results["unused_vars"]:
        results["score"] -= 5
        results["suggestions"].append(f"Unused variables detected: {', '.join(results['unused_vars'])} — remove them.")

    results["score"] = max(0, results["score"])
    return results
