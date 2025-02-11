import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet # type: ignore
from PIL import Image # type: ignore
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, "wb") as file:
        file.write(key)

def load_key(key_file):
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_image(input_image, output_image, key):
    with open(input_image, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_image, "wb") as file:
        file.write(encrypted_data)

def decrypt_image(input_image, output_image, key):
    with open(input_image, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_image, "wb") as file:
        file.write(decrypted_data)

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def encrypt():
    key_file = "key.key"
    input_image = entry.get()
    output_image = input_image.split('.')[0] + "_encrypted." + input_image.split('.')[1]

    if os.path.exists(key_file):
        key = load_key(key_file)
    else:
        key = generate_key()
        save_key(key, key_file)

    encrypt_image(input_image, output_image, key)
    status_label.config(text="Encryption Successful")

def decrypt():
    key_file = "key.key"
    input_image = entry.get()
    output_image = input_image.split('.')[0] + "_decrypted." + input_image.split('.')[1]

    if os.path.exists(key_file):
        key = load_key(key_file)
    else:
        status_label.config(text="Key file not found. Encryption needed first.")
        return

    decrypt_image(input_image, output_image, key)
    status_label.config(text="Decryption Successful")

def about():
    messagebox.showinfo("About", "Image Encryption Tool\n\nThis application allows you to encrypt and decrypt image files using AES encryption.")

def exit_application():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Create GUI
root = tk.Tk()
root.title("Image Encryption Tool")

label = tk.Label(root, text="Select an image file:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

browse_button = tk.Button(root, text="Browse", command=select_image)
browse_button.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

about_button = tk.Button(root, text="About", command=about)
about_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()


#.\venv\Scripts\activate-----------------------activate venv 1st imp. cmd

 #python .\venv\Image_encryptor.py----------------------> 2nd run cmd imp.

# """ PS C:\Users\plilh\Documents\Rohini's documents\Image_Encryptor_pro.py> .\venv\Scripts\activate
# >> 
# (venv) PS C:\Users\plilh\Documents\Rohini's documents\Image_Encryptor_pro.py> python .\venv\Image_encryptor.py
# Exception in Tkinter callback"""