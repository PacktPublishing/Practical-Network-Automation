import socket

def validateipv4ip(address):
    try:
        socket.inet_aton(address)
        print ("Correct IPv4 IP")
    except socket.error:
        print ("wrong IPv4 IP")

def validateipv6ip(address):
    ### for IPv6 IP address validation
    try:
        socket.inet_pton(socket.AF_INET6,address)
        print ("Correct IPv6 IP")
    except socket.error:
        print ("wrong IPv6 IP")

#correct IPs:
validateipv4ip("2.2.2.1")
validateipv6ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")


#Wrong IPs:
validateipv4ip("2.2.2.500")
validateipv6ip("2001:0db8:85a3:0000:0000:8a2e")
