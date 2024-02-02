from crypto import *

import tkinter as tk
from tkinter import ttk, font


def run_app():

    # Encrypt or decrypt based on the button clicked

    def process(action):
        password = password_entry.get()
        if action == 'encrypt':
            text = left_text.get("1.0", tk.END)
            try:
                encrypted_text = encrypt_message(text, password)
                right_text.delete("1.0", tk.END)
                right_text.insert(tk.END, encrypted_text)
            except Exception as e:
                right_text.delete("1.0", tk.END)
                right_text.insert(tk.END, str(e))
        elif action == 'decrypt':
            text = right_text.get("1.0", tk.END)
            try:
                decrypted_text = decrypt_message(text, password)
                left_text.delete("1.0", tk.END)
                left_text.insert(tk.END, decrypted_text)
            except Exception as e:
                left_text.delete("1.0", tk.END)
                left_text.insert(tk.END, str(e))

    # Set up the main window
    root = tk.Tk()
    root.title("Encryption/Decryption Tool")
    root.iconbitmap("key.ico")

    # Use a more modern theme
    style = ttk.Style()
    style.theme_use('clam')  # or 'alt', 'default', 'classic', 'vista'

    # Custom font
    customFont = font.Font(family="Helvetica", size=12)

    # Configure the grid row and column weights
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)
    root.grid_columnconfigure(2, weight=1)

    # Configure the grid row and column weights for the main window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)
    root.grid_columnconfigure(2, weight=1)

    # Create frames for layout
    left_frame = tk.Frame(root, padx=10, pady=10)
    left_frame.grid(row=0, column=0, sticky='nsew')
    right_frame = tk.Frame(root, padx=10, pady=10)
    right_frame.grid(row=0, column=2, sticky='nsew')
    center_frame = tk.Frame(root, padx=10, pady=10)
    center_frame.grid(row=0, column=1, sticky='ns')

    # Configure the grid row and column weights for the frames
    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    # Create text boxes with sticky attributes
    left_text = tk.Text(left_frame, height=10, width=40)
    left_text.grid(row=0, column=0, sticky='nsew')
    right_text = tk.Text(right_frame, height=10, width=40)
    right_text.grid(row=0, column=0, sticky='nsew')

    # Password entry
    password_label = tk.Label(center_frame, text="Password", font=customFont)
    password_label.pack()
    password_entry = ttk.Entry(center_frame, show='*')
    password_entry.pack(pady=5)

    # Buttons for encryption and decryption
    encrypt_button = ttk.Button(
        center_frame, text="Encrypt ->", command=lambda: process('encrypt'))
    encrypt_button.pack(pady=5)
    decrypt_button = ttk.Button(
        center_frame, text="<- Decrypt", command=lambda: process('decrypt'))
    decrypt_button.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    run_app()
