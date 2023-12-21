import socket
import threading


HOST = '127.0.0.1'
PORT = 54321
BUFSIZE = 1024

nickname = input("Enter your nickname: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((HOST, PORT))

    def receive():
        while True:
            try:
                message = clientSocket.recv(BUFSIZE).decode("utf-8")
                if message == "NICK":
                    clientSocket.send(nickname.encode("utf-8"))
                else:
                    print(message)
            except:
                print("Error!!")
                clientSocket.close()
                break

    def write():
        while True:
            message = f"{nickname}: {input()}"
            clientSocket.send(message.encode("utf-8"))

    receiveThread = threading.Thread(target=receive)
    writeThread = threading.Thread(target=write)

    receiveThread.start()
    writeThread.start()

    writeThread.join()
