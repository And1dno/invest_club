import socket
import pickle
import rsa

HOST = 'localhost'
PORT = 8087

# Загрузка ключей сервера из файлов
with open(".public_key_server.txt", "rb") as file:
    server_public_key = file.read()

with open(".private_key_server.txt", "rb") as file:
    server_private_key = file.read()

# Загрузка ключей в объекты rsa.PublicKey и rsa.PrivateKey
server_public_key = rsa.PublicKey.load_pkcs1(server_public_key)
server_private_key = rsa.PrivateKey.load_pkcs1(server_private_key)

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected by', addr)

        # Получаем публичный ключ клиента
        client_public_key_str = conn.recv(1024)
        client_public_key = rsa.PublicKey.load_pkcs1(client_public_key_str)

        # Отправляем публичный ключ сервера клиенту
        conn.send(server_public_key.save_pkcs1())

        # Получаем зашифрованное сообщение от клиента
        encrypted_message = conn.recv(1024)

        # Расшифровываем сообщение с помощью приватного ключа сервера
        message = rsa.decrypt(encrypted_message, server_private_key)
        print("Полученное сообщение:", message.decode())

        # Шифруем ответ публичным ключом клиента
        response = b"Hello client!"
        encrypted_response = rsa.encrypt(response, client_public_key)
        conn.send(encrypted_response)