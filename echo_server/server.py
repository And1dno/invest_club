import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            # Прием данных от клиента
            request = client_socket.recv(1024)
            if not request:
                # Клиент прервал соединение
                break
            print(f"Получено от клиента: {request.decode('utf-8')}")

            # Отправка данных клиенту (эхо)
            client_socket.send(request)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие соединения с клиентом
        print("Закрытие соединения с клиентом.")
        client_socket.close()

def start_server():
    server_ip = "localhost"
    server_port = 12345

    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Сервер запущен на {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключение клиента: {addr[0]}:{addr[1]}")

        # Создание отдельного потока для обработки клиента
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
