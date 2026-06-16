import tkinter as tk

root = tk.Tk()
root.title("Ticket Calculator")

label = tk.Label(root, text="This program calculates the prices for your tickets")
label.pack(padx=30, pady=30)

def on_click():
    label.config(text="Click")
    
button = tk.Button(root, text="Calculate", command=on_click)
button.pack(padx=25, pady=12)

root.mainloop()