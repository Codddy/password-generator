# pip install pyperclip

import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

# Function to generate a random password
def generate_password(length=12, use_symbols=True, use_numbers=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the "Generate Password" button click
def generate_button_clicked():
    password_length = int(password_length_entry.get())
    use_symbols = symbols_var.get()
    use_numbers = numbers_var.get()
    password = generate_password(password_length, use_symbols, use_numbers)
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(0, password)

# Function to handle the "Copy Password" button click
def copy_password_clicked():
    password = generated_password_entry.get()
    pyperclip.copy(password)
    copy_label.config(text="Password copied to clipboard!")
    root.after(2000, clear_copy_label)  # Clear label after 2 seconds

# Function to clear the "Password copied to clipboard!" label
def clear_copy_label():
    copy_label.config(text="")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")  # Set initial window size
root.resizable(False, False)  # Make the window non-resizable

# Create and place GUI elements
password_length_label = ttk.Label(root, text="Password Length:")
password_length_label.pack()

password_length_entry = ttk.Entry(root)
password_length_entry.pack()

symbols_var = tk.BooleanVar()
symbols_checkbutton = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbutton.pack()

numbers_var = tk.BooleanVar()
numbers_checkbutton = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbutton.pack()

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

generated_password_label = ttk.Label(root, text="Generated Password:")
generated_password_label.pack()

generated_password_entry = ttk.Entry(root, width=40)
generated_password_entry.pack()

copy_button = ttk.Button(root, text="Copy Password", command=copy_password_clicked)
copy_button.pack()

copy_label = ttk.Label(root, text="")
copy_label.pack()

# Start the Tkinter event loop
root.mainloop()
