import tkinter as tk
from tkinter import messagebox
import re

try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
    word_list = set(words.words())
except:
    word_list = set()

# Function to check password strength
def check_strength():
    password = entry.get()
    strength_msg = ""
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add an uppercase letter.")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add a lowercase letter.")

    if not re.search(r"[0-9]", password):
        suggestions.append("Add a digit.")

    if not re.search(r"[\W_]", password):
        suggestions.append("Add a special character.")

    if password.lower() in word_list:
        suggestions.append("Avoid using dictionary words.")

    if len(suggestions) == 0:
        strength_msg = "Strong password!"
    elif len(suggestions) <= 2:
        strength_msg = "Moderate password. " + "\n".join(suggestions)
    else:
        strength_msg = "Weak password. " + "\n".join(suggestions)

    messagebox.showinfo("Password Strength", strength_msg)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()


tk.Button(root, text="Check Strength", command=check_strength).pack(pady=20)

root.mainloop()
