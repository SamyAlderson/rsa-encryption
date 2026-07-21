import unittest
from unittest.mock import patch
from src.utils import generate_random_key, check_key_size, encrypt_message, decrypt_message

class TestUtils(unittest.TestCase):

    def test_generate_random_key(self):
        # Ensure generated key is of the correct size
        key = generate_random_key(512)
        self.assertEqual(len(key), 64)  # 512 bits is 64 bytes

        key = generate_random_key(1024)
        self.assertEqual(len(key), 128)  # 1024 bits is 128 bytes

        key = generate_random_key(2048)
        self.assertEqual(len(key), 256)  # 2048 bits is 256 bytes

    def test_check_key_size(self):
        # Test valid key sizes
        self.assertTrue(check_key_size(512))
        self.assertTrue(check_key_size(1024))
        self.assertTrue(check_key_size(2048))

        # Test invalid key sizes
        self.assertFalse(check_key_size(256))
        self.assertFalse(check_key_size(768))

    def test_encrypt_message(self):
        # Test encryption with a valid key
        key = generate_random_key(512)
        message = b"Hello, world!"
        encrypted_message = encrypt_message(key, message)
        self.assertNotEqual(message, encrypted_message)

        # Test encryption with an invalid key
        with self.assertRaises(ValueError):
            encrypt_message(b"invalid_key", message)

    def test_decrypt_message(self):
        # Test decryption with a valid key
        key = generate_random_key(512)
        message = b"Hello, world!"
        encrypted_message = encrypt_message(key, message)
        decrypted_message = decrypt_message(key, encrypted_message)
        self.assertEqual(message, decrypted_message)

        # Test decryption with an invalid key
        with self.assertRaises(ValueError):
            decrypt_message(b"invalid_key", encrypted_message)

    @patch('src.utils.generate_random_key')
    def test_encrypt_message_invalid_key(self, mock_generate_random_key):
        # Test encryption with an invalid key
        mock_generate_random_key.return_value = b"invalid_key"
        with self.assertRaises(ValueError):
            encrypt_message(b"invalid_key", b"message")

    @patch('src.utils.generate_random_key')
    def test_decrypt_message_invalid_key(self, mock_generate_random_key):
        # Test decryption with an invalid key
        mock_generate_random_key.return_value = b"invalid_key"
        with self.assertRaises(ValueError):
            decrypt_message(b"invalid_key", b"encrypted_message")

if __name__ == '__main__':
    unittest.main()