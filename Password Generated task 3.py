

#  A password generator     
import tkinter as tk
from tkinter import messagebox
import random
import string

# Password Generator Function
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Length must be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="lightblue")

# Heading
heading = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="lightblue")
heading.pack(pady=10)

# Length Entry
length_frame = tk.Frame(root, bg="lightblue")
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Enter password length:", bg="lightblue")
length_label.pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side=tk.LEFT)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Courier", 14), bg="lightblue", fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()