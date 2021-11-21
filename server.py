import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
distinctClients = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print("Exception occured ",str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Remote Procedure Call Server'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
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
    start_new_thread(threaded_client, (Client, ))
    distinctClients += 1
    print('Thread Number: ' + str(distinctClients))
    
ServerSocket.close()
