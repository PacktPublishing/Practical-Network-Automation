import socket
import re

def validateipv4ip(address):
    try:
        socket.inet_aton(address)
    except socket.error:
        print ("wrong IPv4 IP",address)

def validateipv6ip(address):
    ### for IPv6 IP address validation
    try:
        socket.inet_pton(socket.AF_INET6,address)
    except socket.error:
        print ("wrong IPv6 IP", address)

        
sampletext="""
ip tacacs server 10.10.10.10
int fa0/1
ip address 25.25.25.298 255.255.255.255
no shut
ip name-server 100.100.100.200
int fa0/0
ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334
ip logging host 90.90.91.92
int te0/2
ipv6 address 2602:306:78c5:6a40:421e:6813:d55:ce7f
no shut
exit

"""

sampletext=sampletext.split("\n")
for line in sampletext:
    if ("ipv6" in line):
        ipaddress=re.search("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))",line)
        validateipv6ip(ipaddress.group(0))
    elif(re.search("\d+.\d+.\d+.\d+",line)):
        ipaddress=re.search("\d+.\d+.\d+.\d+",line)
        validateipv4ip(ipaddress.group(0))
