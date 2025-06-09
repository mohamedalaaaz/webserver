from socket import *
from threading import Thread

# Server settings
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Listen for up to 5 connections

print(f"Multithreaded Web Server is running on port {serverPort}...")

def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        print(f"\nReceived request from {addr}:\n{message}")

        if len(message.split()) < 2:
            raise ValueError("Malformed or incomplete request")

        filename = message.split()[1]
        if filename == '/':
            filename = '/index.html'
        filepath = filename[1:]

        with open(filepath, 'r') as f:
            outputdata = f.read()

        responseHeader = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        connectionSocket.send(responseHeader.encode())
        connectionSocket.send(outputdata.encode())

    except FileNotFoundError:
        errorMessage = 'HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>'
        connectionSocket.send(errorMessage.encode())
        print(errorMessage)

    except ValueError as e:
        errorMessage = f'HTTP/1.1 400 Bad Request\r\n\r\n<html><body><h1>400 Bad Request</h1><p>{e}</p></body></html>'
        connectionSocket.send(errorMessage.encode())
        print(errorMessage)

    finally:
        connectionSocket.close()
        print(f"Connection with {addr} closed.")

while True:
    print("\nReady to serve...")
    connectionSocket, addr = serverSocket.accept()
    # Create and start a new thread for each client
    clientThread = Thread(target=handle_client, args=(connectionSocket, addr))
    clientThread.start()