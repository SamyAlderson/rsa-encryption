# src/main.py

import argparse
from src.utils import generate_keypair, encrypt, decrypt
from src.rsa import RSAError

def main():
    parser = argparse.ArgumentParser(description="RSA encryption tool")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate public and private keys")
    parser.add_argument("-e", "--encrypt", help="Encrypt message using public key")
    parser.add_argument("-d", "--decrypt", help="Decrypt message using private key")
    parser.add_argument("-k", "--key-size", type=int, choices=[512, 1024, 2048], help="Key size (bits)")
    args = parser.parse_args()

    if args.generate:
        key_size = args.key_size or 2048
        public_key, private_key = generate_keypair(key_size)
        print("Public key:", public_key)
        print("Private key:", private_key)
    elif args.encrypt:
        try:
            encrypted = encrypt(args.encrypt, args.key_size)
            print("Encrypted message:", encrypted)
        except RSAError as e:
            print(f"Error: {e}")
    elif args.decrypt:
        try:
            decrypted = decrypt(args.decrypt, args.key_size)
            print("Decrypted message:", decrypted)
        except RSAError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()