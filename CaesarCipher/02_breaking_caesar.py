# LAB 1, Ex1, Task 3: Breaking Caesar Cipher
# Goal: Break the Caesar Cipher and recover the plaintext
# Author: [Your Name]
# Student-ID: [Your Student ID]

import time
from caesar_cipher import CaesarCipher

# implement a brute force attack function, 
# that goes through all the possible keys
def brute_force_caesar(ciphertext):
    possible_plaintexts = []
    
    # Your code goes here :)
        
    return possible_plaintexts

if __name__ == "__main__":
    ciphertext = "IYE RKFO NYXO GOVV DY VOKBX DRSC DOMRXSAEO. LED DRSXQ GSVV QOD WYBO NSPPSMEVD - KNWSX"
    start_time = time.time()
    results = brute_force_caesar(ciphertext)
    end_time = time.time()

    print("Brute force results:")
    for key, plaintext in results:
        print(f"Key {key}: {plaintext}")

    print(f"\nTime taken: {end_time - start_time:.8f} seconds")