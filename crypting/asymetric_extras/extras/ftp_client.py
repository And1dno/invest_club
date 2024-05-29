import socket
import rsa

HOST = 'localhost'
PORT = 21  # FTP порт

def load_key(file_path, is_public=True):
    with open(file_path, "rb") as file:
        key_data = file.read()
    if is_public:
        return rsa.PublicKey.load_pkcs1(key_data)
    else:
        return rsa.PrivateKey.load_pkcs1(key_data)

def send_public_key(sock, public_key):
    sock.send(public_key.save_pkcs1())

def receive_public_key(sock):
    key_data = sock.recv(1024)
    return rsa.PublicKey.load_pkcs1(key_data)

def encrypt_message(message, public_key):
    return rsa.encrypt(message, public_key)

def decrypt_message(encrypted_message, private_key):
    return rsa.decrypt(encrypted_message, private_key)

client_public_key = load_key(".public_key_client.txt", is_public=True)
client_private_key = load_key(".private_key_client.txt", is_public=False)

with socket.socket() as sock:
    sock.connect((HOST, PORT))

    send_public_key(sock, client_public_key)
    server_public_key = receive_public_key(sock)

    command = "LIST"  # Пример FTP-команды
    encrypted_command = encrypt_message(command.encode(), server_public_key)
    sock.send(encrypted_command)

    encrypted_response = sock.recv(1024)
    response = decrypt_message(encrypted_response, client_private_key)
    print("FTP Response:", response.decode())

    quit_command = "QUIT"
    encrypted_quit = encrypt_message(quit_command.encode(), server_public_key)
    sock.send(encrypted_quit)
