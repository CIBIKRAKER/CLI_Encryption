#Features of this projct:
#Reading files
#Encrypting files
#Decrypting files
#Writing files that are encrypted or decrypted

from cryptography.fernet import Fernet
import os


if not os.path.exists("filekey.key"):
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as f:
        f.write(key)
else:
    with open("filekey.key", "rb") as f:
        key = f.read()

fernet = Fernet(key)

choice = input("Enter 1 for encrypting or 2 for decrypting: ")

if choice == "1":
    with open("test.txt", "rb") as f:
        original = f.read()
    encrypted = fernet.encrypt(original)
    with open("test.txt", "wb") as f:
        f.write(encrypted)
    print("File encrypted.")
elif choice == "2":
    with open("test.txt", "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    with open("test.txt", "wb") as f:
        f.write(decrypted)
    print("File decrypted.")
else:
    print("Invalid input.")
