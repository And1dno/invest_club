import socket
from random import randint

# Shared prime number and generator
p = 23
g = 5

# Generate client's private key
a = randint(1, 20)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    # Calculate client's public key
    A = (g ** a) % p
    client_socket.send(str(A).encode())
    print("Sent client's public key:", A)

    # Receive server's public key
    B = int(client_socket.recv(1024).decode())
    print("Received server's public key:", B)

    # Compute shared secret
    client_shared_secret = (B ** a) % p
    print("Shared secret at client:", client_shared_secret)

    client_socket.close()

if __name__ == "__main__":
    start_client()