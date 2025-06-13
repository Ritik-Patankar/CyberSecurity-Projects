import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def load_key(path):
    with open(path, "rb") as f:
        return RSA.import_key(f.read())

# Load private key
server_key = load_key("server_private.pem")
cipher_rsa = PKCS1_OAEP.new(server_key)

# Setup socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Server listening...")
conn, addr = server_socket.accept()
print("Connection from", addr)

while True:
    encrypted_data = conn.recv(1024)
    if not encrypted_data:
        break
    try:
        decrypted_data = cipher_rsa.decrypt(encrypted_data)
        print("Client:", decrypted_data.decode())
        response = input("You: ")
        conn.send(response.encode())
    except Exception as e:
        print("Decryption error:", e)
        break

conn.close()
server_socket.close()
