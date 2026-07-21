# rsa-encryption

A simple implementation of RSA encryption in Python.

## What and Why

This project provides a basic implementation of RSA encryption in Python, allowing users to generate public and private keys, encrypt and decrypt messages.

## Features

* Generate public and private keys
* Encrypt and decrypt messages using RSA
* Handle key sizes of 512, 1024, and 2048 bits

## Install

To install the project, run the following command:

```bash
pip install cryptography
```

Then, install the project's dependencies using pip:

```bash
pip install .
```

## Usage

To generate public and private keys, run the following command:

```bash
python src/main.py --generate-keys
```

To encrypt a message, run the following command:

```bash
python src/main.py --encrypt --key-size 2048 --message "Hello, World!"
```

To decrypt an encrypted message, run the following command:

```bash
python src/main.py --decrypt --key-size 2048 --encrypted-message "your_encrypted_message_here"
```

## Build from Source

To build the project from source, run the following command:

```bash
python setup.py install
```

## Project Structure

```markdown
rsa-encryption/
    README.md
    setup.py
    pyproject.toml
    src/
        main.py
        utils.py
        rsa.py
    tests/
        test_rsa.py
        test_utils.py
```

## License

This project is licensed under the MIT License.
```