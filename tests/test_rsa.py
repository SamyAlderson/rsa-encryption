# tests/test_rsa.py

import unittest
from src.utils import generate_keys
from src.rsa import encrypt, decrypt

class TestRSA(unittest.TestCase):

    def test_generate_keys(self):
        # Generate a key pair and store the public and private keys
        public_key, private_key = generate_keys(2048)
        self.assertIsNotNone(public_key)
        self.assertIsNotNone(private_key)

    def test_encrypt_decrypt(self):
        # Generate a key pair
        public_key, private_key = generate_keys(2048)

        # Encrypt a message using the public key
        message = b"Hello, World!"
        encrypted_message = encrypt(public_key, message)
        self.assertIsNotNone(encrypted_message)

        # Decrypt the message using the private key
        decrypted_message = decrypt(private_key, encrypted_message)
        self.assertEqual(message, decrypted_message)

    def test_encrypt_invalid_key(self):
        # Try to encrypt a message with an invalid public key
        public_key = None
        message = b"Hello, World!"
        with self.assertRaises(ValueError):
            encrypt(public_key, message)

    def test_decrypt_invalid_key(self):
        # Try to decrypt a message with an invalid private key
        private_key = None
        encrypted_message = b"Encrypted message"
        with self.assertRaises(ValueError):
            decrypt(private_key, encrypted_message)

if __name__ == '__main__':
    unittest.main()