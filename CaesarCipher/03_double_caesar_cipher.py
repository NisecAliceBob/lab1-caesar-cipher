# LAB 1, Ex2: Double Caesar Cipher
# Goal: Implementing the Double Caesar Cipher and encrypt/decrypt using two keys
# Author: [Your Name]
# Student-ID: [Your Student ID]

from caesar_cipher import CaesarCipher

def double_caesar_cipher(ciphertext, key1, key2):
    caesar1 = CaesarCipher(key1)
    caesar2 = CaesarCipher(key2)
    result = ""
    
    # Your code goes here :)

    return result


def main():
    print("Double Caesar Cipher")
        
    key1 = 13
    key2 = 9
    ciphertext = "PDA BENOP NQHA KB BECDP YHQX EO UKQ ZKJ'P PWHG WXKQP BECDP YHQX"
    plaintext = double_caesar_cipher(ciphertext, key1, key2)
    print(f"Result: {plaintext}")


if __name__ == "__main__":
    main()

