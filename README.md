[Web Server Documentation.pdf](https://github.com/user-attachments/files/20660696/Web.Server.Documentation.pdf)
Web Server Project Documentation
Overview:
The Web Server Project is a basic implementation of server-client architecture in Python
using the socket module. It demonstrates the creation of a TCP server that can handle
HTTP GET requests and respond to them with appropriate HTTP responses. The
corresponding HTTP client enables testing by sending requests to the server and displaying
its responses.
Objective:
Develop a basic web server in Python that:
• Accepts and parses HTTP GET requests.
• Serves HTML files stored in the server directory.
• Sends a proper HTTP response including headers and file content.
• Returns a 404 error if the requested file is not found.
---
Technology Used:
• Language: Python 3
• Module:
o socket from the Python standard library
o sys to obtain server_host server_port filename from the command line
---
How It Works:
1. Server (server.py)
Below is the high-level flow of the web server:
1. Create a socket and bind it to the specified host and port.
2. Start listening for client connections using listen().
3. Accept incoming connections using accept() and process requests.
4. Parse incoming HTTP GET requests.
5. Locate the requested file:
o If found, return the file content with an HTTP 200 response.
o If not found, return a meaningful HTTP 404 error message.
6. Close the connection after responding.
2. Client (client.py)
Below is the high-level flow of the HTTP client:
1. Parse command-line arguments for the server address, port, and filename.
2. Create a TCP client socket and connect to the server.
3. Construct and send an HTTP GET request for the specified file.
4. Receive and display the HTTP response from the server.
5. Close the connection.
Error Handling:
1. Server-Side:
o Returns a 404 Not Found error for missing files or invalid paths.
o Handles unexpected errors gracefully with generic error messages.
2. Client-Side:
o Handles connection errors if the server is not running or unavailable.
o Validates command-line arguments to ensure proper format.
How to Run from a Browser:
1. Save the Python server code as web_server.py.
2. Place an HTML file (e.g., HelloWorld.html) in the same directory.
3. Run the script using: python web_server.py
4. Open a browser on another device in the same network and visit:
http://< Server-IP>:6789/HelloWorld.html
5. To test the 404 error, try accessing a file that does not exist.
