#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:26:23 2024

@author: wangtingwei
"""
from library import generate_keys, encrypt, decrypt



def main():
    public_key = None
    private_key = None

    while True:
        print("\n1. Generate Private and Public Keys")
        print("2. Encrypt a Message")
        print("3. Decrypt a Message")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            public_key, private_key = generate_keys()
            print("Public Key: ", public_key)
            print("Private Key: ", private_key)
        elif choice == '2':
            if public_key is None:
                print("Generate keys first.")
                continue
            message = input("Enter a message to encrypt: ")
            encrypted_msg = encrypt(message, *public_key)  # Assuming public_key is a tuple (e, n)
            with open("encrypted.txt", "w") as file:
                file.write(' '.join(map(str, encrypted_msg)))
            print("Encrypted Message written to 'encrypted.txt'")
        elif choice == '3':
            if private_key is None:
                print("Generate keys and encrypt a message first.")
                continue
            try:
                with open("encrypted.txt", "r") as file:
                    encrypted_msg = list(map(int, file.read().strip().split()))
                decrypted_msg = decrypt(encrypted_msg, private_key[0], private_key[1])  # private_key = (d, n)
                print("Decrypted Message: ", decrypted_msg)
            except FileNotFoundError:
                print("Encrypted file not found. Encrypt a message first.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
