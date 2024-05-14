import socket
from random import randint

# Shared prime number and generator
p = 23
g = 5

# Generate server's private key
b = randint(1, 20)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(1)
    print("Server is listening on port 8000...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive client's public key
        A = int(conn.recv(1024).decode())
        print("Received client's public key:", A)

        # Calculate server's public key
        B = (g ** b) % p
        conn.send(str(B).encode())
        print("Sent server's public key:", B)

        # Compute shared secret
        server_shared_secret = (A ** b) % p
        print("Shared secret at server:", server_shared_secret)

        conn.close()

if __name__ == "__main__":
    start_server()