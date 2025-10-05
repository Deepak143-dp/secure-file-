import tkinter as tk
from tkinter import filedialog
from crypto_utils import generate_key, encrypt_file, decrypt_file

def select_file():
    return filedialog.askopenfilename()

def encrypt_selected_file():
    file_path = select_file()
    if file_path:
        passphrase = entry_passphrase.get()
        key = generate_key(passphrase)
        if encrypt_file(file_path, key):
            lbl_status.config(text="File encrypted successfully.")

def decrypt_selected_file():
    file_path = select_file()
    if file_path:
        passphrase = entry_passphrase.get()
        key = generate_key(passphrase)
        if decrypt_file(file_path, key):
            lbl_status.config(text="File decrypted successfully.")

# GUI setup
root = tk.Tk()
root.title("CIPHER VAULT")
root.configure(bg="#121212")  # Dark background

main_frame = tk.Frame(root, bg="#121212")
main_frame.pack(padx=20, pady=10)

lbl_passphrase = tk.Label(main_frame, text="Enter Password:", bg="#121212", fg="white")
lbl_passphrase.grid(row=0, column=0, padx=5, pady=5, sticky='e')

entry_passphrase = tk.Entry(main_frame, show="*", bg="#373737", fg="white")
entry_passphrase.grid(row=0, column=1, padx=5, pady=5)

btn_encrypt = tk.Button(main_frame, text="Encrypt File", command=encrypt_selected_file, bg="#004e98", fg="white")
btn_encrypt.grid(row=1, column=0, padx=5, pady=5, sticky='we')

btn_decrypt = tk.Button(main_frame, text="Decrypt File", command=decrypt_selected_file, bg="#004e98", fg="white")
btn_decrypt.grid(row=1, column=1, padx=5, pady=5, sticky='we')

lbl_status = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#121212", fg="white")
lbl_status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
