import socket
import os

# Рабочая директория
WORK_DIR = '/invest_club/lowlevel_web'


def handle_client(conn):
    request = conn.recv(1024).decode()
    print(request)

    # Разбор запроса
    lines = request.split('\n')
    method, path, _ = lines[0].split(' ')
    if method == 'GET':
        if path == '/':
            file_path = os.path.join(WORK_DIR, 'templates/index.html')
        else:
            file_path = os.path.join(WORK_DIR, path.lstrip('/'))

        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                response = f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{content.decode()}'
                conn.send(response.encode())
        except FileNotFoundError:
            response = 'HTTP/1.1 404 Not Found\n\n'
            conn.send(response.encode())
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n'
        conn.send(response.encode())

    conn.close()


def start_server(port=8081):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f'Server started on port {port}')

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected: {addr}")
        handle_client(conn)


if __name__ == '__main__':
    start_server()
