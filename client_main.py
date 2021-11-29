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
    print("Connected to server")
except socket.error as e:
    print(str(e))

#recieves response of size 1024 bytes
Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
print("Request for available functions ")
ClientSocket.send(str.encode("BROADCAST"))
Response = ClientSocket.recv(1024);
broadcast = eval(Response.decode("utf-8"))
bcL = broadcast.items()

while True:

    print("Available functions are:")
    c =1
    for i,j in bcL:s
        print(c,":",i,"\n"+str(j))
        c+=1

    clinetIp = input("Choose a function")
    dict2 = {}
    print("Press s to send rpc request")
    choice = input()
    if choice == 's':
        dict2['call'] = len(dict2.items())
        print(dict2)
    else:
        dicVal = int(choice)-1
        k,j =list(dic1.items())[dicVal]
        j = [i for i in input('Enter parameters: ')]
        dict2[k] = j

while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    #Decodes response to UTF-8 format
    print(Response.decode('utf-8'))

ClientSocket.close()
