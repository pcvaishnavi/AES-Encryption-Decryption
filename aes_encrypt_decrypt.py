from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

class AESCipher:
    def __init__(self, key):
        # Ensure the key is 16, 24, or 32 bytes long
        self.key = key.ljust(32)[:32].encode()

    def encrypt_file(self, input_file, output_file):
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv  # Initialization vector

        with open(input_file, 'rb') as f:
            plaintext = f.read()

        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        with open(output_file, 'wb') as f:
            f.write(iv + ciphertext)

        print(f"File encrypted successfully: {output_file}")

    def decrypt_file(self, input_file, output_file):
        with open(input_file, 'rb') as f:
            iv = f.read(16)  # Read IV first
            ciphertext = f.read()

        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(output_file, 'wb') as f:
            f.write(plaintext)

        print(f"File decrypted successfully: {output_file}")

# Example usage
if __name__ == "__main__":
    key = "my_secret_key_123"  # Change this to a secure key
    aes_cipher = AESCipher(key)

    # Encrypt file
    aes_cipher.encrypt_file("example.txt", "encrypted.bin")

    # Decrypt file
    aes_cipher.decrypt_file("encrypted.bin", "decrypted.txt")
