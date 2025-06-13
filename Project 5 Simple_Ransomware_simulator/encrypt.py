import os
from cryptography.fernet import Fernet

# Clean setup
folder = "sample_files"
os.makedirs(folder, exist_ok=True)

# Create files
for i in range(3):
    with open(os.path.join(folder, f"file{i+1}.txt"), "w") as f:
        f.write(f"This is sample file {i+1}")

# Generate key
key = Fernet.generate_key()
with open("secret.key", "wb") as f:
    f.write(key)

fernet = Fernet(key)

# Encrypt files
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    with open(path, "rb") as f:
        data = f.read()
    with open(path, "wb") as f:
        f.write(fernet.encrypt(data))

print("Files encrypted. Now run decrypt.py.")
