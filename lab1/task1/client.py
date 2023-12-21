import socket


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        message = input("Your message: ")
        socket.send(message.encode('utf-8'))

        if message.lower() == "bye":
            break

        serverAnswer = socket.recv(BUFSIZE).decode('utf-8')
        print(f"Server: {serverAnswer}")
