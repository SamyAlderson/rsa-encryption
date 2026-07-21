# src/utils.py

import random
import string

def generate_keypair(bits: int) -> tuple:
    """
    Generate a random RSA keypair of the given size in bits.
    
    :param bits: The size of the key in bits (512, 1024, or 2048).
    :return: A tuple containing the public key and private key.
    """
    if bits not in [512, 1024, 2048]:
        raise ValueError("Invalid key size. Must be 512, 1024, or 2048 bits.")
    
    # Generate two random prime numbers for the RSA key
    p = random_prime(bits // 2)
    q = random_prime((bits + 1) // 2)
    
    # Calculate the modulus and the totient function
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose a random number e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    # Calculate d such that d*e ≡ 1 (mod phi)
    d = mod_inverse(e, phi)
    
    # Return the public key (e, n) and the private key (d, n)
    return ((e, n), (d, n))


def random_prime(bits: int) -> int:
    """
    Generate a random prime number of the given size in bits.
    
    :param bits: The size of the prime number in bits.
    :return: A random prime number.
    """
    while True:
        # Generate a random number of the given size in bits
        n = random.getrandbits(bits)
        
        # Check if the number is prime
        if is_prime(n):
            return n


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
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


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two numbers.
    
    :param a: The first number.
    :param b: The second number.
    :return: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a: int, m: int) -> int:
    """
    Calculate the modular inverse of a number.
    
    :param a: The number to find the modular inverse of.
    :param m: The modulus.
    :return: The modular inverse of a.
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = extended_gcd(b % a, a)
            return g, y - (b // a) * x, x
    
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % m