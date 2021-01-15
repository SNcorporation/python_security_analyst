#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("Enter the IP address of host you want to scan port for: ")
port = int(input("Enter the port number you want to scan: "))
s.settimeout(5)
if s.connect_ex((host, port)):
    print("Port is closed")
else:
    print("Port is open")

