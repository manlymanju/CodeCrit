# CodeCrit — Intelligent Python Code Reviewer

**CodeCrit** is a lightweight, human-built Python static analyzer that reviews Python scripts and provides readable feedback on code quality, readability, and common issues.  
Designed for students and beginners to learn better code hygiene.

## Features
- Static code analysis using Python's `ast` module
- Detects loops, functions, print statements, long lines (>80 chars)
- Basic unused variable detection
- Scoring (0–100) and friendly rating messages
- CLI mode (main.py) and optional GUI (gui_app.py)
- Saves a human-readable report to `results/report.txt`

## Quickstart (Windows / VS Code)
1. Clone or download this repo.
2. Open folder in VS Code.
3. Run (in terminal):
```bash
python main.py
