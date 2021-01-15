#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))
    

def main():   
    ip = input("Enter the IP: ")
    port = str(input("Enter the Port: "))
    banner(ip, port)

main()