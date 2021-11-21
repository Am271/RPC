import socket

ClientSocket = socket.socket()
#Enter IP address and port number of host
host = ''
port = 

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#recieves response of size 1024 bytes
Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    #Decodes response to UTF-8 format
    print(Response.decode('utf-8'))

ClientSocket.close()
