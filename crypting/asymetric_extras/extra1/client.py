import socket
import pickle
import rsa

HOST = 'localhost'
PORT = 8087

# Чтение ключей из файлов как байтовых строк
with open(".public_key_client.txt", "rb") as file:
    public_key_str = file.read()

with open(".private_key_client.txt", "rb") as file:
    private_key_str = file.read()

# Загрузка ключей из байтовых строк в объекты rsa.PublicKey и rsa.PrivateKey
client_public_key = rsa.PublicKey.load_pkcs1(public_key_str)
client_private_key = rsa.PrivateKey.load_pkcs1(private_key_str)

with socket.socket() as sock:
    sock.connect((HOST, PORT))

    # Отправляем публичный ключ клиента серверу
    sock.send(client_public_key.save_pkcs1())

    # Принимаем открытый ключ сервера
    server_public_key_str = sock.recv(1024)
    server_public_key = rsa.PublicKey.load_pkcs1(server_public_key_str)

    # Шифруем сообщение публичным ключом сервера
    message = b"Secret message"
    encrypted = rsa.encrypt(message, server_public_key)
    sock.send(encrypted)

    # Принимаем зашифрованный ответ от сервера
    encrypted_response = sock.recv(1024)

    # Дешифруем ответ с помощью приватного ключа клиента
    response = rsa.decrypt(encrypted_response, client_private_key)
    print("Ответ:", response.decode())