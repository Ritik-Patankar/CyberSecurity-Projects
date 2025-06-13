import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def load_key(path):
    with open(path, "rb") as f:
        return RSA.import_key(f.read())

# Load public key
server_public_key = load_key("server_public.pem")
cipher_rsa = PKCS1_OAEP.new(server_public_key)

# Setup socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    encrypted_msg = cipher_rsa.encrypt(msg.encode())
    client_socket.send(encrypted_msg)
    response = client_socket.recv(1024)
    print("Server:", response.decode())

client_socket.close()
