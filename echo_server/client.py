'''import socket

def start_client():
    server_ip = "localhost"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    print(f"Соединение с сервером {server_ip}:{server_port}")

    try:
        while True:
            message = input("Введите строку для отправки серверу: ")
            client_socket.send(message.encode('utf-8'))

            # Прием данных от сервера
            response = client_socket.recv(1024)
            print(f"Получено от сервера: {response.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nРазрыв соединения с сервером.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
'''