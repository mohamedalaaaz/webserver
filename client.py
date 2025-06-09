import sys
from socket import *


if len(sys.argv) != 4:
    print("Usage: client.py server_host server_port filename")
    sys.exit(1)


server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

try:

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((server_host, server_port))

    http_request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

    clientSocket.send(http_request.encode())

    response = clientSocket.recv(1024)

    print("Response from server:")
    print(response.decode())


except Exception as e:
    print(f"Error occurred: {e}")

finally:
    clientSocket.close()

