from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from tkinter import messagebox

def generate_key(passphrase):
    key = hashlib.sha256(passphrase.encode()).digest()  # 32 bytes key for AES-256
    return key



def encrypt_file(file_path, key):
    try:
        cipher = AES.new(key, AES.MODE_CBC)
        with open(file_path, 'rb') as file:
            plaintext = file.read()
        padded_plaintext = pad(plaintext, AES.block_size)
        ciphertext = cipher.iv + cipher.encrypt(padded_plaintext)
        with open(file_path + '.enc', 'wb') as file:
            file.write(ciphertext)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            ciphertext = file.read()
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
        with open(file_path[:-4], 'wb') as file:
            file.write(plaintext)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False
