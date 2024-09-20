import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")

            # parsing the client message for the operation and arguments
            strdata = data.decode("utf-8")
            operation = strdata[0]
            
            if operation != '+' and operation != '*':
                result_message = "The client message is not correctly formatted. The only supported operations are add and multiply." # should this message also be sent to the client? should there be an error thrown?
                print(f"sending result message '{result_message}' back to client")
                conn.sendall(result_message.encode('utf-8'))
                break
            print(f"requested operation is {operation}")
            
            args = strdata[1:]
            args = args.strip()
            args = args.split(":")

            try:
                for i in range(len(args)):
                    args[i] = int(args[i])
            except ValueError:
                result_message = "The arguments must be integers."
                print(f"sending result message '{result_message}' back to client")
                conn.sendall(result_message.encode('utf-8'))
                break

            if len(args) < 2:
                result_message = "There must be at least 2 inputted arguments."
                print(f"sending result message '{result_message}' back to client")
                conn.sendall(result_message.encode('utf-8'))
                break

            print(f"request includes {len(args)} arguments: {args}")

            # calculating the result of the operation and making the result message
            result_message = ""
            if operation == "+":
                result = 0
                for arg in args: 
                    result += arg
                for i in range(len(args)-1):
                    result_message += str(args[i]) + "+"
            else:
                result = 1
                for arg in args:
                    result *= arg
                for i in range(len(args)-1):
                    result_message += str(args[i]) + "*"
            
            print(f"result of operation: {result}")
        
            result_message += str(args[len(args)-1]) + "=" + str(result)
            print(f"sending result message '{result_message}' back to client")

            conn.sendall(result_message.encode('utf-8'))

print("server is done!")