# Was gonna make a ping sweep and append all found addresses to a txt file
# While you can use an IP as a target in remote shutdown, I got a better idea

# We are on a Windows network, and Windows uses NetBIOS to resolve hostnames
# so just scan the network for valid NetBIOS names and append them to the target file!

import os
t = list(range(0,255))
for i in t:
    #print("192.168.0."+str(i))
    os.system("ping 192.168.0."+str(i)+" -c 1")
    #os.system(ping IP.IP.IP."+str(i)+" /s 1")
