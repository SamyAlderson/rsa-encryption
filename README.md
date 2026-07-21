# rsa-encryption
## Practical RSA implementation in Python

This is a basic RSA encryption library that generates public and private keys for secure message exchange. It's a learning aid for understanding RSA fundamentals and its use in secure communication.

### Install
```bash
pip install rsa-encryption
```
### Usage
```python
import rsa_encryption

public_key, private_key = rsa_encryption.generate_keys(2048)
encrypted_message = rsa_encryption.encrypt("Hello, World!", public_key)
decrypted_message = rsa_encryption.decrypt(encrypted_message, private_key)
print(decrypted_message)  # Output: Hello, World!
```
### Build from Source
```bash
git clone https://github.com/SamyAlderson/rsa-encryption.git
cd rsa-encryption
pip install -e .
```
### Run Tests
```bash
python -m unittest discover -s tests
```
### Project Structure
```markdown
rsa-encryption/
rsa_encryption.py
test_rsa_encryption.py
tests/
test_rsa_encryption_test.py
utils.py
keys.py
__init__.py
README.md
LICENSE
```
### License
Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.