"""
Script to encrypt and decrypt text using the Vigenère cipher. A GUI is provided to enter the text, the key and the mode (encrypt or decrypt).
(I fucking love cryptography!)
Maximilian
06.06.2024
❤
"""

##################################################
#                    Imports                     #
##################################################

import tkinter as tk
import customtkinter as ctk


##################################################
#                     Code                       #
##################################################

def vigenere_cipher(text, key, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    keyIndex = 0
    key = key.upper()

    for symbol in text:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated += LETTERS[num]
            elif symbol.islower():
                translated += LETTERS[num].lower()

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated += symbol
    return translated

def main():
    window = tk.Tk()
    window.title("Vigenère Cipher")

    mode_label = tk.Label(window, text="Wählen Sie 'encrypt' oder 'decrypt':")
    mode_label.pack()
    mode_entry = ctk.CTkEntry(window)
    mode_entry.pack()

    text_label = tk.Label(window, text="Geben Sie Ihren Text ein:")
    text_label.pack()
    text_entry = ctk.CTkEntry(window)
    text_entry.pack()

    key_label = tk.Label(window, text="Geben Sie den Schlüssel ein:")
    key_label.pack()
    key_entry = ctk.CTkEntry(window, show="*")
    key_entry.pack()

    result_label = tk.Label(window, text="Ergebnis:")
    result_label.pack()
    result_text = tk.Text(window)
    result_text.pack()

    def process():
        mode = mode_entry.get()
        message = text_entry.get()
        key = 'YOUR_SECRET_KEY'  # Setzen hier deinen Schlüssel ein
        user_key = key_entry.get()

        if user_key == key:
            if mode.lower() in ['encrypt', 'decrypt']:
                result = vigenere_cipher(message, key, mode.lower())
                result_text.insert(tk.END, result)
            else:
                result_text.insert(tk.END, "Ungültiger Modus. Wählen Sie 'encrypt' oder 'decrypt'.")
        else:
            result_text.insert(tk.END, "Falscher Schlüssel!")

    process_button = ctk.CTkButton(window, text="Verarbeiten", command=process)
    process_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()