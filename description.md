# Jessica Klurfeld CSC 249 – Project 1 – Simple RPC Client-Server App

## Overview of Application
This is a simple math server that handles the addition and mulitplication operations.

## Client -> Server Message Format
The user input is of the format {operation} {arguments}, where there are at least two integer arguments and each argument is separated by one space with no trailing whitespace. The two implemented operations are "add" and "mulitply." An example of correctly formatted user input is "add 12 3 5". 

This then gets encoded as the operation being the symbol + or * and each integer argument is separated by a colon. For example "add 12 3 5" becomes "+12:3:5".

## Server -> Client Message Format
The server to client message format is each argument separated by the operation then = the result. For example, given the client message "+12:3:5", the server would send the result message "12+3+5=20". There are also various error messages that the client can receive such as "There must be at least 2 inputted arguments." if the user inputs less than 2 arguments.

## Example Output

### Client Trace

```
$ python3 math-client.py
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
What message would you like to send to the server? add 12 3 5
sending request: +12:3:5
message sent, waiting for reply
Received response: 'b'12+3+5=20'' [9 bytes]
client is done!
```

### Server Trace

```
$ python3 math-server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 49806)
Received client message: 'b'+12:3:5'' [7 bytes]
requested operation is +
request includes 3 arguments: [12, 3, 5]
result of operation: 20
sending result message '12+3+5=20' back to client
server is done!
```

## References
https://stackoverflow.com/questions/606191/convert-bytes-to-a-string-in-python-3