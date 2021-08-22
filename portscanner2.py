#!/bin/python3
import sys, socket
from datetime import datetime
from termcolor import colored
#Accept user input
ipAdrress = input("Enter the Ip address to scan: ")
print("Target IP: "+ipAdrress)
startingPort = input("Enter first port: ")
print("Starting port: "+ startingPort)
endPort = input("Enter last port: ")
print("Last port: "+endPort)

#define target
target = socket.gethostbyname(ipAdrress)
try:
    for port in range(int(startingPort), int(endPort)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print("Checking port {}".format(port))
        if result == 0:
            print (colored("Port {} is open.".format(port),'green'))
        s.close()
except KeyboardInterrupt:
    print("\n Terminating scan......")
    sys.exit()
except socket.gaierror:
    print("Host could not be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to server")
    sys.exit()