import socket
import threading

HOST = "127.0.0.1"
PORT = 54321
BUFSIZE = 1024

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(clientSocket):
    while True:
        try:
            message = clientSocket.recv(BUFSIZE)
            broadcast(message)
        except:
            index = clients.index(clientSocket)
            clients.remove(clientSocket)
            clientSocket.close()
            broadcast(f">>{nicknames[index]} left the chat<<".encode("utf-8"))
            nicknames.remove(nicknames[index])
            break


def receive(serverSocket):
    while True:
        clientSocket, address = serverSocket.accept()
        print(f'Got a connection from {address}')

        clientSocket.send("NICK".encode("utf-8"))
        nickname = clientSocket.recv(BUFSIZE).decode("utf-8")

        nicknames.append(nickname)
        clients.append(clientSocket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f">>{nickname} joined the chat<<".encode("utf-8"))
        clientSocket.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(clientSocket,))
        thread.start()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    print('The server is waiting for connection...')
    receive(serverSocket)
