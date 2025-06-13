from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)

# Save private key
private_key = key.export_key()
with open("server_private.pem", "wb") as priv_file:
    priv_file.write(private_key)

# Save public key
public_key = key.publickey().export_key()
with open("server_public.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("RSA key pair generated.")
