import socket
import rsa
import pickle
import threading

HOST = 'localhost'
PORT_INIT = 8087
PORT_POOL = [8090, 8091, 8092, 8093]  # Пул портов для основного общения

def load_key(file_path, is_public=True):
    with open(file_path, "rb") as file:
        key_data = file.read()
    if is_public:
        return rsa.PublicKey.load_pkcs1(key_data)
    else:
        return rsa.PrivateKey.load_pkcs1(key_data)

def send_public_key(conn, public_key):
    conn.send(public_key.save_pkcs1())

def receive_public_key(conn):
    key_data = conn.recv(1024)
    return rsa.PublicKey.load_pkcs1(key_data)

def encrypt_message(message, public_key):
    return rsa.encrypt(message, public_key)

def decrypt_message(encrypted_message, private_key):
    return rsa.decrypt(encrypted_message, private_key)

def is_allowed_key(client_public_key):
    with open("allowed_keys.txt", "rb") as file:
        allowed_keys = pickle.load(file)
    return client_public_key in allowed_keys

def handle_client(conn, addr):
    print('Connected by', addr)

    client_public_key = receive_public_key(conn)
    if not is_allowed_key(client_public_key):
        print("Unauthorized client key. Disconnecting.")
        conn.close()
        return

    send_public_key(conn, server_public_key)

    encrypted_port_message = conn.recv(1024)
    new_port = int(decrypt_message(encrypted_port_message, server_private_key).decode())

    if new_port not in PORT_POOL:
        print("Invalid port requested by client. Disconnecting.")
        conn.close()
        return

    print(f"Switching to port {new_port} for further communication.")
    conn.send(encrypt_message(b'OK', client_public_key))
    conn.close()

    with socket.socket() as new_sock:
        new_sock.bind((HOST, new_port))
        new_sock.listen()
        new_conn, new_addr = new_sock.accept()
        with new_conn:
            print('Reconnected by', new_addr)
            encrypted_message = new_conn.recv(1024)

            message = decrypt_message(encrypted_message, server_private_key)
            print("Received message:", message.decode())

            response = b"Hello client!"
            encrypted_response = encrypt_message(response, client_public_key)
            new_conn.send(encrypted_response)

def ftp_handle_client(conn, addr, server_private_key):
    print(f"FTP Connected by {addr}")

    client_public_key = receive_public_key(conn)
    send_public_key(conn, server_public_key)

    while True:
        encrypted_message = conn.recv(1024)
        if not encrypted_message:
            break

        message = decrypt_message(encrypted_message, server_private_key).decode()
        print(f"FTP Received: {message}")

        if message == "QUIT":
            response = b"Goodbye!"
            encrypted_response = encrypt_message(response, client_public_key)
            conn.send(encrypted_response)
            break
        else:
            response = b"Command received"
            encrypted_response = encrypt_message(response, client_public_key)
            conn.send(encrypted_response)

    conn.close()

server_public_key = load_key(".public_key_server.txt", is_public=True)
server_private_key = load_key(".private_key_server.txt", is_public=False)

def main():
    with socket.socket() as sock:
        sock.bind((HOST, PORT_INIT))
        sock.listen()
        print("Initial server started")

        while True:
            conn, addr = sock.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def start_ftp_server():
    with socket.socket() as server_socket:
        server_socket.bind((HOST, 21))
        server_socket.listen()
        print("FTP server started")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=ftp_handle_client, args=(conn, addr, server_private_key)).start()

if __name__ == "__main__":
    threading.Thread(target=main).start()
    threading.Thread(target=start_ftp_server).start()
