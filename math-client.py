import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
# MSG = "+2:3:1"

print("client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established")
    msg = input("What message would you like to send to the server? ")

    # encodes message to send to server
    input = msg.split(" ")
    converted_msg = ""
    if input[0] == "add":
        converted_msg += "+"
    elif input[0] == "multiply":
        converted_msg += "*"
    for i in range(1, len(input)-1):
        converted_msg += str(input[i]) + ":"
    converted_msg += input[len(input)-1]
    print(f"sending request: {converted_msg}")
    s.sendall(bytes(converted_msg, 'utf-8'))
    print("message sent, waiting for reply")
    data = s.recv(1024)

print(f"Received response: '{data!r}' [{len(data)} bytes]")
print("client is done!")