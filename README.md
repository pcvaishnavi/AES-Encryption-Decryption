# AES Encryption & Decryption

## Overview
This project provides a simple implementation of **AES encryption and decryption** using Python. It allows users to securely encrypt and decrypt files using the **AES (Advanced Encryption Standard)** algorithm in **CBC (Cipher Block Chaining) mode**.

## Features
- Encrypts any file using **AES-256 encryption**.
- Decrypts files back to their original state.
- Uses a secure **initialization vector (IV)** for encryption.
- Ensures safe file handling with proper padding.

## Requirements
Make sure you have Python installed on your system.

### Install Dependencies
This project uses the `PyCryptodome` library. Install it using:
```bash
pip install pycryptodome
```

## Usage

### 1️⃣ Create a Sample File to Encrypt
Create a text file named `example.txt` in the project directory and add some sample text:
```text
This is a secret message.
Only authorized users should be able to read this after decryption.
Encryption ensures data security.
```

### 2️⃣ Run the Encryption & Decryption Script
Run the Python script in VS Code or a terminal:
```bash
python aes_encrypt_decrypt.py
```

### 3️⃣ Expected Output
When you run the script, it will:
- Encrypt `example.txt` into `encrypted.bin`
- Decrypt `encrypted.bin` back to `decrypted.txt`

You should see this in the terminal:
```bash
File encrypted successfully: encrypted.bin
File decrypted successfully: decrypted.txt
```

### 4️⃣ Check the Files
- `encrypted.bin` → **Binary file** (encrypted, unreadable)
- `decrypted.txt` → **Matches `example.txt` exactly**

## Project Structure
```
AES-Encryption-Decryption/
│── aes_encrypt_decrypt.py  # Main script
│── example.txt             # Original file (to encrypt)
│── encrypted.bin           # Encrypted file (output)
│── decrypted.txt           # Decrypted file (output)
│── README.md               # Documentation
```

## Troubleshooting
✅ **If `decrypted.txt` does not match `example.txt`**:
- Make sure you are using a **consistent encryption key**.
- Delete `encrypted.bin` and `decrypted.txt` and **rerun the script**.
- Ensure `PyCryptodome` is installed correctly.

## Contribution
Contributions are welcome! If you'd like to improve this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Submit a Pull Request.

### 🚀 Happy Encrypting! Let me know if you need improvements. 😊

