import socket
import sys

ClientSocket = socket.socket()
#Enter IP address and port number of host
if not len(sys.argv) > 2:
    print('IP address/Port number not specified! Use as: $ python3 server.py <ip-address> <port>')
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#recieves response of size 1024 bytes
Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    #Decodes response to UTF-8 format
    print(Response.decode('utf-8'))

ClientSocket.close()
