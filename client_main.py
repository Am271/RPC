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
dict2 = {}

while True:

    print("----->Available functions are<-----")
    c =1
    for i,j in bcL:
        print(c,":",i,"\t"+str(j))
        c+=1

    print("-->Choose a function<--")
    print("Press s to send rpc request")
    choice = input('> ')
    if choice == 's':
        dict2['call'] = len(dict2.items())
        # print(dict2)
        ClientSocket.send(str.encode(str(dict2)))
        dict2 = {}
        dict2 = eval(ClientSocket.recv(1024))
        print("----->Results<-----")
        for i in range(dict2.get('results')):
            k, v = list(dict2.items())[i + 2]
            print(k, ':', dict2.get(k))
        if(dict2.get('errors')):
            print('The following functions have a wrong list of parameters')
            for i in dict2.get('errors'):
                print(i)
        dict2 = {}
    else:
        dicVal = int(choice) - 1
        k,j =list(broadcast.items())[dicVal]
        j = [i for i in input('Enter parameters: ').split()]
        # print(k, j)
        dict2[k] = j

# while True:
#     Input = input('Say Something: ')
#     ClientSocket.send(str.encode(Input))
#     Response = ClientSocket.recv(1024)
#     #Decodes response to UTF-8 format
#     print(Response.decode('utf-8'))

ClientSocket.close()
