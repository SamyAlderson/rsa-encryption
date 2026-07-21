# src/rsa.py

import hashlib
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

class RSA:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """Generate public and private keys."""
        key = serialization.generate_private_key(
            algorithm=hashes.SHA256(),
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        self.public_key = key.public_key()
        self.private_key = key

    def public_key_string(self):
        """Return public key as PEM string."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def private_key_string(self):
        """Return private key as PEM string."""
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

    def encrypt(self, message):
        """Encrypt message using public key."""
        try:
            encrypted_message = self.public_key.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return encrypted_message
        except Exception as e:
            raise ValueError(f"Failed to encrypt message: {e}")

    def decrypt(self, encrypted_message):
        """Decrypt encrypted message using private key."""
        try:
            decrypted_message = self.private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted_message
        except InvalidSignature:
            raise ValueError("Invalid signature")
        except Exception as e:
            raise ValueError(f"Failed to decrypt message: {e}")

    def sign(self, message):
        """Sign message using private key."""
        try:
            signature = self.private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            raise ValueError(f"Failed to sign message: {e}")

    def verify(self, message, signature, public_key):
        """Verify signature of message using public key."""
        try:
            public_key.load_pem_public_key(signature)
            return True
        except Exception as e:
            return False