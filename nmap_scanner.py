#!/usr/bin/pyhton3

import nmap

scanner = nmap.PortScanner()

ip_addr = input("Please enter the IP Address of System you want to perform scan: ")
type(ip_addr)
print('<------------------------------------------------------------------------->')

scan_type = input("""\nPlease enter the scan type: 
                    1) SYNC ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan \n""")

print("Performing selected option ",scan_type,"scan on ",ip_addr)

if scan_type == '1':
    print("Nmap Version is: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP Status is: ",scanner[ip_addr].state())
    print("Protocols are: ",scanner[ip_addr].all_protocols())
    print("Open Ports are: ",scanner[ip_addr]['tcp'].keys())
elif scan_type == '2':
    print("Nmap Version is: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP Status is: ",scanner[ip_addr].state())
    print("Protocols are: ",scanner[ip_addr].all_protocols())
    print("Open Ports are: ",scanner[ip_addr]['udp'].keys())
elif scan_type == '3':
    print("Nmap Version is: ",scanner.nmap_version())
    print(scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O'))
    print(scanner.scaninfo())
    print("IP Status is: ",scanner[ip_addr].state())
    print("Protocols are: ",scanner[ip_addr].all_protocols())
    print("Open Ports are: ",scanner[ip_addr]['tcp'].keys())
    #print("OS Detection is: ",scanner[ip_addr].mac())
    #print("OS Detection is: ",scanner[ip_addr].osfamily())
else:
    print("Please Enter a valid option \n")