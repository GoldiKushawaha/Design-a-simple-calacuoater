# Design a simple calacuoater

import tkinter as tk

# Function to evaluate expressions
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons in grid
row_val = 1
col_val = 0

for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, font="Arial 18", height=2, width=5)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the app
root.mainloop()