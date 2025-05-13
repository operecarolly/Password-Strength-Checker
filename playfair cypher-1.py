import tkinter as tk
from tkinter import messagebox

def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key_set = set()
    matrix = []
    
    for char in key.upper():
        if char not in key_set and char.isalpha():
            key_set.add(char)
            matrix.append(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_set:
            key_set.add(char)
            matrix.append(char)
    
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.replace("J", "I").upper()
    text = ''.join([char for char in text if char.isalpha()])
    
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    
    encrypted_text = ""
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted_text

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper()
    
    pairs = [(text[i], text[i+1]) for i in range(0, len(text), 2)]
    decrypted_text = ""
    
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return decrypted_text

def encrypt_text():
    key = key_entry.get()
    plaintext = text_entry.get()
    if not key or not plaintext:
        messagebox.showwarning("Input Error", "Please enter both key and text")
        return
    encrypted_text = playfair_encrypt(plaintext, key)
    result_label.config(text=f"Encrypted Text: {encrypted_text}")

def decrypt_text():
    key = key_entry.get()
    ciphertext = text_entry.get()
    if not key or not ciphertext:
        messagebox.showwarning("Input Error", "Please enter both key and text")
        return
    decrypted_text = playfair_decrypt(ciphertext, key)
    result_label.config(text=f"Decrypted Text: {decrypted_text}")

# GUI Setup
root = tk.Tk()
root.title("Playfair Cipher")
root.geometry("400x300")

tk.Label(root, text="Enter Key:").pack()
key_entry = tk.Entry(root)
key_entry.pack()

tk.Label(root, text="Enter Text:").pack()
text_entry = tk.Entry(root)
text_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()