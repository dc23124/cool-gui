import tkinter as tk
from tkinter import messagebox

items = ["Party Hat", "Confetti", "Balloons"]


# Returns the user's input
def return_input():
    return {
        "name": entry_name.get().strip(),
        "receipt": entry_receipt.get().strip(),
        "item": selected_item.get(),
        "amount": entry_amount.get().strip()
    }


def get_input():
    data = return_input()

    name = data["name"]
    receipt = data["receipt"]
    item = data["item"]
    amount = data["amount"]

    # Name validation
    if not name.replace(" ", "").isalpha():
        messagebox.showwarning("Input Error", "Please enter your full name.")
        return

    # Receipt validation
    if not receipt.isdigit():
        messagebox.showwarning("Input Error", "Receipt number must contain only numbers.")
        return

    # Amount validation
    if not amount.isdigit():
        messagebox.showwarning("Input Error", "Amount must be a positive whole number.")
        return

    amount = int(amount)

    if amount <= 0:
        messagebox.showwarning("Input Error", "Amount must be greater than 0.")
        return

    output = (
        f"Full Name: {name}\n"
        f"Receipt Number: {receipt}\n"
        f"Item Hired: {item}\n"
        f"Amount: {amount}"
    )

    messagebox.showinfo("Success", output)


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_receipt.delete(0, tk.END)
    selected_item.set(items[0])
    entry_amount.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Cool GUI")
root.geometry("400x400")

# Name
tk.Label(root, text="Full name required:").grid(padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(padx=10, pady=5)

# Receipt
tk.Label(root, text="Enter receipt number:").grid(padx=10, pady=5)
entry_receipt = tk.Entry(root, width=30)
entry_receipt.grid(padx=10, pady=5)

# Item
tk.Label(root, text="Select an item:").grid(padx=10, pady=5)

selected_item = tk.StringVar(value=items[0])

item_menu = tk.OptionMenu(root, selected_item, *items)
item_menu.grid(padx=10, pady=5)

# Amount
tk.Label(root, text="Enter the amount of items:").grid(padx=10, pady=5)
entry_amount = tk.Entry(root, width=30)
entry_amount.grid(padx=10, pady=5)

# Buttons
tk.Button(root, text="Clear All", command=clear_entries).grid(padx=10, pady=5)
tk.Button(root, text="Submit", command=get_input).grid(padx=10, pady=20)

root.mainloop()