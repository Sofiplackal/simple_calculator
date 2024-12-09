import tkinter as tk

# Function to update the expression in the entry box
def button_click(value):
    current = entry.get()
    
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to backspace (remove the last character)
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set window size and prevent resizing
root.geometry("400x600")
root.resizable(False, False)

# Set background color
root.configure(bg="lightblue")  # Set the background color of the window

# Create the entry widget to display the expression/result
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="solid", justify="right", bg="lightyellow")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Define button layout and design
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 1), (".", 4, 2), ("C", 4, 0), ("+", 4, 3),
    ("=", 5, 0), ("⌫", 5, 1)  # Backspace button labeled as "⌫"
]

# Define button styles
button_style = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "bd": 3,
    "relief": "raised",
    "fg": "black"
}

# Create the buttons and place them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, command=evaluate, **button_style, bg="orange")
    elif text == "C":
        button = tk.Button(root, text=text, command=clear, **button_style, bg="red")
    elif text == "⌫":
        button = tk.Button(root, text=text, command=backspace, **button_style, bg="yellow")
    else:
        button = tk.Button(root, text=text, command=lambda value=text: button_click(value), **button_style)
    button.grid(row=row, column=col, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()