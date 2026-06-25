import tkinter as tk
from tkinter import messagebox

def get_input():
    user_text = entry.get().strip()  # Get text and remove extra spaces
    if not user_text:
        messagebox.showwarning("Input Required", "Please enter your full name.")
    
#main window
root = tk.Tk()
root.title("Cool GUI")
root.geometry("400x400")

# input field sizes
entry = tk.Entry(root, width=30)
entry.grid(padx=10, pady=10)

label = tk.Label(root, text="Full name required: ")
label.grid(padx=10, pady=10)

label2 = tk.Label(root, text="Enter receipt number: ")
label2.grid(padx=10, pady=10)

label3 = tk.Label(root, text="The item that is hired required: ")
label3.grid(padx=10, pady=10)

label4 = tk.Label(root, text="Enter the amount of items: ")
label4.grid(padx=10, pady=10)

root.mainloop()

# To ensure good data collection the following are required

# · Customer full name required

# · Receipt number any number

# · The item that is hired required

# · How many of the item the customer has hired between 1 and 50