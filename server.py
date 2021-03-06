import socket
import os, sys
from _thread import *
import stub

ServerSocket = socket.socket()
#Enter host IP address and port number
if not len(sys.argv) > 1:
    print('Port number not specified! Use as: $ python3 server.py <port>')
    sys.exit()

host = ''
port = int(sys.argv[1])
distinctClients = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print("Exception occured ",str(e))
    sys.exit()

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection, addr):
    connection.send(str.encode('Welcome to the Remote Procedure Call Server'))
    while True:
        data = connection.recv(2048)
        req = data.decode('utf-8')
        if req == 'BROADCAST':

            # Calls the broadcast function from to stub to obtain and send all the available methods
            print('Broadcast received from client, sending method list and description')
            reply = stub.broadcast()
        else:
            # process() in stub returns a tuple containing the status code of operation and
            # attempts to perform the method call and return the result
            print('RPC request received from', addr[0])
            result = stub.process(req)
            
            reply = result # Result message or JSON

        if not data:
            break
        connection.sendall(str.encode(reply))
        #Send data from reply until all bytes are sent
    connection.close()

while True:
    #Getting client IP address and port
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    #Creating new thread for new client
    start_new_thread(threaded_client, (Client, address))
    distinctClients += 1
    print('Thread Number: ' + str(distinctClients))
    
ServerSocket.close()
