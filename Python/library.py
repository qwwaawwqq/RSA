#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:25:15 2024

@author: wangtingwei
"""

import random

def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime(length=50):
    """Generate a prime number of 'length' bits."""
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def powmod(base, exp, mod):
    """Efficiently compute (base ** exp) % mod using exponentiation by squaring."""
    result = 1
    base = base % mod  # Ensure base is within mod to prevent unnecessary large numbers
    while exp > 0:
        if exp % 2 == 1:  # If exponent is odd, multiply the base with the result
            result = (result * base) % mod
        base = (base * base) % mod  # Square the base
        exp //= 2
    return result

def find_modular_inverse(e, phi):
    """Find the modular inverse of e under modulo phi using the Extended Euclidean Algorithm."""
    if gcd(e, phi) != 1:
        return None  # No modular inverse if e and phi are not coprime

    m0, y, x = phi, 0, 1
    while e > 1:
        # q is quotient
        q = e // phi
        t = phi

        # phi is remainder now, process same as Euclid's algo
        phi = e % phi
        e = t
        t = y

        # Update y and x
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x += m0

    return x

def generate_keys():
    """Generate RSA keys."""
    p = generate_prime(10)
    q = generate_prime(10)
    if p == q:
        q = generate_prime(10)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = find_modular_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, e, n):
    """Encrypt the message by converting each character to its ASCII value,
       encrypting it and then storing each encrypted character."""
    encrypted_msg = []
    for char in message:
        encrypted_char = powmod(ord(char), e, n)  # Ensure powmod handles large integers appropriately
        encrypted_msg.append(encrypted_char)
    return encrypted_msg

def decrypt(encrypted_msg, d, n):
    """Decrypt the encrypted message by converting each encrypted ASCII back
       to its original character after decryption."""
    decrypted_msg = []
    for char in encrypted_msg:
        # Decrypt using modular exponentiation
        decrypted_char = chr(powmod(char, d, n))
        decrypted_msg.append(decrypted_char)
    return ''.join(decrypted_msg)
