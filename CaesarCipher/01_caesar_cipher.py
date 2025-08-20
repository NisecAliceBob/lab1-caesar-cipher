# LAB 1, Ex1, Task 2: Caesar Cipher
# Goal: Implementing the Caesar Cipher encryption and decryption
# Author: [Your Name]
# Student-ID: [Your Student ID]

from caesar_cipher import CaesarCipher
    
def main():
    print("Caesar Cipher Program")
    mode = input("Enter mode (enc/dec): ").strip().lower()
    if mode not in ['enc', 'dec']:
        print("Invalid mode selected. Please choose 'enc' or 'dec'.")
        return
    
    try:
        key = int(input("Enter the key (integer): ").strip())
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    # You should implement the Caesar Cipher class,
    # To do so, please open the caesar_cipher.py file
    # and implement the class with the required methods
    # after that, you can simply run this file and get the result
    Caesar = CaesarCipher(key)
    
    text = input("Enter the text: ").strip()
    if mode == "enc":
        ciphertext = Caesar.encrypt(text)
        print(f"ciphertext: {ciphertext}")
    else:
        plaintext = Caesar.decrypt(text)
        print(f"plaintext: {plaintext}")
 
if __name__ == "__main__":
    main()