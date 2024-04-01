import socket

def start_client():
    server_ip = "localhost"
    server_port = 2004

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    print(f"Соединение с сервером {server_ip}:{server_port}")

    try:
        while True:
            message = input("Введите строку для отправки серверу: ")
            client_socket.send(message.encode('utf-8'))
            print(f"Отправлено на сервер: {message}")

            # Прием данных от сервера
            response = client_socket.recv(1024)
            if (response.decode('utf-8')=="Соединение разорвано"):
                break
            else:
                print(f"Получено от сервера: {response.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nРазрыв соединения с сервером.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
