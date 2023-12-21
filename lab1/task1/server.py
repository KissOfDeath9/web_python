import socket
import datetime
import time


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 8


def clearBuffer(sock):
    sock.setblocking(False)
    try:
        while sock.recv(BUFSIZE):
            pass
    except:
        sock.setblocking(True)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)
    print('The server is waiting for connection...')

    while True:
        clientSocket, clientAddress = serverSocket.accept()
        print(f'Got a connection from {clientAddress}')

        while True:
            clientMessage = clientSocket.recv(BUFSIZE)
            decodedMessage = clientMessage.decode("utf-8")
            print(f'Message: {decodedMessage} Time: {datetime.datetime.now()}')

            if decodedMessage.lower() == "bye":
                break

            time.sleep(5)

            if len(clientMessage) == BUFSIZE:
                clientSocket.send("The message is too long".encode('utf-8'))
                clearBuffer(clientSocket)
            else:
                clientSocket.send(clientMessage)

        clientSocket.close()
        print(f'{clientAddress} has been disconnected')
