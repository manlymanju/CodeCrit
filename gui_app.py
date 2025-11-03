# gui_app.py - simple Tkinter GUI for CodeCrit
import tkinter as tk
from tkinter import filedialog
from analyzer import analyze_code
from feedback_generator import generate_feedback

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if not path:
        return
    analysis = analyze_code(path)
    feedback = generate_feedback(analysis)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, feedback)

root = tk.Tk()
root.title("CodeCrit — Python Code Reviewer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

btn = tk.Button(frame, text="📁 Browse Python File", command=browse_file)
btn.pack(pady=5)

text_box = tk.Text(frame, width=80, height=25)
text_box.pack()

root.mainloop()
