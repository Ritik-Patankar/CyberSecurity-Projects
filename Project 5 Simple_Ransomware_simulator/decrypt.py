import os
from cryptography.fernet import Fernet

folder = "sample_files"

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(filepath, "wb") as f:
            f.write(decrypted)
