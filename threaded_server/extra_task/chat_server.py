import socket
import threading


class Server:
<<<<<<< HEAD:extra_task/chat_server.py
    def __init__(self, host='192.168.56.1', port=55555):
=======
    def __init__(self, host='127.0.0.1', port=55555):
>>>>>>> 7ba3ea5c3f467e6ca9d65e9ff3a002d27a6e26c0:threaded_server/extra_task/chat_server.py
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []
        self.message_history = []

    def broadcast(self, message, sender):
        self.message_history.append((sender, message))
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message, self.nicknames[self.clients.index(client)])
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat!'.encode('ascii'), "Server")
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Nickname of the client is {nickname}!")
            self.broadcast(f"{nickname} joined the chat!".encode('ascii'), "Server")
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()


server = Server()
server.receive()
