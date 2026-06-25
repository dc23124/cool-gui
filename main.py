import tkinter as tk
from tkinter import messagebox

def get_input():
    name = entry_name.get().strip()
    receipt = entry_receipt.get().strip()
    item = entry_item.get().strip()
    amount = entry_amount.get().strip()

    if not name:
        messagebox.showwarning("Input Required", "Please enter your full name.")
        return

    output = (
        f"Full Name: {name}\n"
        f"Receipt Number: {receipt}\n"
        f"Item Hired: {item}\n"
        f"Amount: {amount}"
    )

    messagebox.showinfo("Done", output)

# main window
root = tk.Tk()
root.title("Cool GUI")
root.geometry("400x400")

# labels + entry fields
label_name = tk.Label(root, text="Full name required:")
label_name.grid(padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(padx=10, pady=5)

label_receipt = tk.Label(root, text="Enter receipt number:")
label_receipt.grid(padx=10, pady=5)
entry_receipt = tk.Entry(root, width=30)
entry_receipt.grid(padx=10, pady=5)

label_item = tk.Label(root, text="The item that is hired:")
label_item.grid(padx=10, pady=5)
entry_item = tk.Entry(root, width=30)
entry_item.grid(padx=10, pady=5)

label_amount = tk.Label(root, text="Enter the amount of items:")
label_amount.grid(padx=10, pady=5)
entry_amount = tk.Entry(root, width=30)
entry_amount.grid(padx=10, pady=5)

# button to submit
submit_btn = tk.Button(root, text="Submit", command=get_input)
submit_btn.grid(padx=10, pady=20)

root.mainloop()