#
# labscanner.py - Kyle
#
# Scans network for hosts with port 135 (RPC) open and grabs their IP and FQDN assigned by the Domain Controller
# The computer must have connected to the domain at some point or else port 135 will not be open
#
# Copyright 2022 Kyle Smith
# Licensed under GPL-3.0-or-later

import socket

network = '192.168.0.'

def IsUp(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    if not s.connect_ex((addr,80)):
        s.close()
        return 1
    else:
        s.close()

# TODO: Un-YanDev this mess
datstrip = str(input("Do you want IPs, FQDNs, or both? (i or f or b): "))
if datstrip == 'i':
    with open(r"/home/ks/targets.txt", "w") as f:
        for i in range(1,255):
            # TODO: Make this supporrt the complete Class B range
            addr = network + str(i)
            if IsUp(addr):
                f.write("%s\n" %(addr))
                print("%s" %(addr))
elif datstrip == 'f':
    with open(r"/home/ks/targets.txt", "w") as f:
        for i in range(1,255):
            # TODO: Make this supporrt the complete Class B range
            addr = network + str(i)
            if IsUp(addr):
                f.write("%s\n" %(socket.getfqdn(addr)))
                print("%s" %(socket.getfqdn(addr)))
elif datstrip == 'b':
    with open(r"/home/ks/targets.txt", "w") as f:
        for i in range(1,255):
            # TODO: Make this supporrt the complete Class B range
            addr = network + str(i)
            if IsUp(addr):
                f.write("%s \t= %s\n" %(addr, socket.getfqdn(addr)))
                print("%s \t= %s" %(addr, socket.getfqdn(addr)))
else:
    print("Invalid option: \'"+str(datstrip)+"\' exiting...")
    exit(1)

print("Scan saved to: "+str(f.name))
