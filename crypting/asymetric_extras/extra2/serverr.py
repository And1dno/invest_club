import socket
import pickle
import rsa
import create_keys

HOST = 'localhost'
PORT = 8087

# Загрузка ключей сервера из файлов
private_key_str=create_keys.Keygen.write_private_key_from_file("server")
public_key_str=create_keys.Keygen.write_public_key_from_file("server")

# Загрузка ключей в объекты rsa.PublicKey и rsa.PrivateKey
public_key = rsa.PublicKey.load_pkcs1(public_key_str)
private_key = rsa.PrivateKey.load_pkcs1(private_key_str)

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
        conn.send(public_key.save_pkcs1())

        # Получаем зашифрованное сообщение от клиента
        encrypted_message = conn.recv(1024)

        # Расшифровываем сообщение с помощью приватного ключа сервера
        message = rsa.decrypt(encrypted_message, private_key)
        print("Полученное сообщение:", message.decode())

        # Шифруем ответ публичным ключом клиента
        response = b"Hello client!"
        encrypted_response = rsa.encrypt(response, client_public_key)
        conn.send(encrypted_response)