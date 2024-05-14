import socket
import threading

HOST = 'localhost'
PORT = 12344

def handle_client(conn, addr):
    print('Подключен клиент:', addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Клиент {addr} отправил: {data.decode()}')
            conn.sendall(data)
            print(f'Клиент {addr} получил: {data.decode()}')

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Сервер запущен...")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 7ba3ea5c3f467e6ca9d65e9ff3a002d27a6e26c0
