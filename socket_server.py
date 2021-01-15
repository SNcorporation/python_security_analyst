#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port= 444

serversocket.bind((host,port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("connection established from %s" % str(address))

    message = "Welcome to my first socket server program \r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
