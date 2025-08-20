# LAB 1, Ex1, Task 2: Caesar Cipher
# Goal: Implementing the Caesar Cipher encryption and decryption
# Author: [Your Name]
# Student-ID: [Your Student ID]

import sys
from caesar_cipher import CaesarCipher
    
def main(mode, key, text):
    print("Caesar Cipher Program")
    print(f"Mode: {mode}")
    print(f"Key: {key}")
    print(f"Text: {text}")
    
    if mode not in ['enc', 'dec']:
        print("Invalid mode selected. Please choose 'enc' or 'dec'.")
        return
    
    try:
        key = int(key)
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    # You should implement the Caesar Cipher class first,
    # then you can simply run this file and get the result
    # To do so, please open the caesar_cipher.py file
    # and implement the class with the required methods
    Caesar = CaesarCipher(key)
    
    if mode == "enc":
        ciphertext = Caesar.encrypt(text)
        print(f"ciphertext: {ciphertext}")
    else:
        plaintext = Caesar.decrypt(text)
        print(f"plaintext: {plaintext}")
 
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 01_caesar_cipher.py <mode> <key> <text>")
        sys.exit(1)
        
    mode = sys.argv[1].strip().lower()
    key = sys.argv[2]
    text = sys.argv[3].strip()
    
    main(mode, key, text)
    