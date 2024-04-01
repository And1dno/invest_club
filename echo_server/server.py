import socket
import threading


def client_handler(client_socket):
    request = client_socket.recv(1024)
    print(f"Сообщение от клиента: {request.decode('utf-8')}")

    if (request.decode('utf-8')!="exit"):
        client_socket.send(request)
    else:
        client_socket.send("Соединение разорвано")
        client_socket.close()


def start_server():
    server_ip = "localhost"
    server_port = 2004

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

    server_socket.listen(7)
    print(f"Сервер запущен на {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключение клиента: {addr[0]}:{addr[1]}")

        # Создание отдельного потока для обработки клиента
        client = threading.Thread(target=client_handler, args=(client_socket,))
        client.start()


if __name__ == "__main__":
    start_server()
