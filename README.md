# CLI_Encryption

A simple Python command-line tool to encrypt and decrypt files using the Fernet symmetric encryption from the `cryptography` library.

## Features
- Read files
- Encrypt files
- Decrypt files
- Write encrypted or decrypted files
- Simple CLI interface

## Requirements
- Python 3.x
- Module: `cryptography`

## Installation & Usage
Clone the repository and run the script:

    git clone https://github.com/CIBIKRAKER/CLI_Encryption.git
    cd CLI_Encryption
    python main.py

Follow the on-screen prompt:
1. Enter `1` to encrypt `test.txt`
2. Enter `2` to decrypt `test.txt`

The encryption key is automatically generated and stored in `filekey.key`.
