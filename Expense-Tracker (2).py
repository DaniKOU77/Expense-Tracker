import tkinter as tk
from tkinter import messagebox
import json

# Initialize the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")
root.configure(bg="black")

# List to store expenses
expenses = []

# Function to load expenses from a file
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

# Function to save expenses to a file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

# Function to add a new expense
def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if not description or not amount or not category:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    if description.isdigit() or category.isdigit():
        messagebox.showerror("Error", "Description and Category must not be numeric!")
        return

    expenses.append({"description": description, "amount": amount, "category": category})
    console_output.insert(tk.END, f"Expense Added: {description} - {amount} ({category})\n")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

# Function to display all expenses
def view_expenses():
    if not expenses:
        messagebox.showinfo("No Expenses", "No expenses to display!")
        return

    console_output.pack()  # Show the console if hidden
    console_output.insert(tk.END, "\n--- Expenses ---\n")
    total = 0
    for expense in expenses:
        console_output.insert(tk.END, f"{expense['description']} - {expense['amount']} ({expense['category']})\n")
        total += expense['amount']
    console_output.insert(tk.END, f"\nTotal: {total}\n")

# Function to create a rounded button
def create_rounded_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", bd=0)
    button.config(height=2, width=20)
    button.pack(pady=15)
    return button

# Function to create a rounded Entry widget
def create_rounded_entry(parent, font, width):
    entry = tk.Entry(parent, font=font, fg="#333", bg="#fff", insertbackground="#333", width=width, relief="solid", bd=2)
    entry.config(highlightbackground="#4CAF50", highlightthickness=2)
    entry.pack(pady=5)
    return entry

# UI Elements

# Title
title_label = tk.Label(root, text="Expense Tracker", font=("Helvetica", 20, "bold"), fg="#fff", bg="black")
title_label.pack(pady=20)

# Description
description_label = tk.Label(root, text="Description", font=("Helvetica", 12), fg="#fff", bg="black")
description_label.pack(pady=5)
description_entry = create_rounded_entry(root, ("Helvetica", 12), 40)

# Amount
amount_label = tk.Label(root, text="Amount", font=("Helvetica", 12), fg="#fff", bg="black")
amount_label.pack(pady=5)
amount_entry = create_rounded_entry(root, ("Helvetica", 12), 40)

# Category
category_label = tk.Label(root, text="Category", font=("Helvetica", 12), fg="#fff", bg="black")
category_label.pack(pady=5)
category_entry = create_rounded_entry(root, ("Helvetica", 12), 40)

# Add Expense Button
add_button = create_rounded_button(root, "Add Expense", add_expense)

# View Expenses Button
view_button = create_rounded_button(root, "View Expenses", view_expenses)

# Command-line style output console (expanded)
console_output = tk.Text(root, height=15, width=70, bg="#333", fg="#00FF00", font=("Courier", 10), relief="flat", bd=0)
console_output.pack(pady=15)
console_output.pack_forget()  # Hide the console by default

# Load expenses on startup
load_expenses()

# Run the application
root.mainloop()

# Save expenses on exit
save_expenses()
