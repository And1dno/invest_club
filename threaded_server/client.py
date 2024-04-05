import socket
import threading

HOST = 'localhost'
PORT = 12344
clients = []
current_client = None

def client_thread():
    global current_client
    while True:
        message = input(
            "Введите сообщение для сервера (или 'switch' для переключения клиента, 'exit' для завершения): ")
        if message == 'exit':
            break
        elif message == 'switch':
            current_client = switch_client()
            continue
        current_client.sendall(message.encode())
        data = current_client.recv(1024)
        print('Получено от сервера:', data.decode())
    current_client.close()

def switch_client():
    print("Доступные клиенты:")
    for i, client in enumerate(clients):
        print(f"{i + 1}: {client}")
    while True:
        choice = input("Введите номер клиента, на который хотите переключиться: ")
        if choice.isdigit() and 0 < int(choice) <= len(clients):
            return clients[int(choice) - 1]
        else:
            print("Некорректный ввод. Пожалуйста, введите номер доступного клиента.")

def main():
    global current_client
    num_clients = int(input("Введите количество клиентов: "))

    for _ in range(num_clients):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        clients.append(client_socket)
    current_client = clients[0]
    thread = threading.Thread(target=client_thread)
    thread.start()

    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

if __name__ == "__main__":
    main()
