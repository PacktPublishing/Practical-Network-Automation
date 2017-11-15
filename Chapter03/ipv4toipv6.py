import ipaddress

def convertusingipaddress(ipv4address):
    print(ipaddress.IPv6Address('2002::' + ipv4address).compressed)

convertusingipaddress("10.10.10.10")
convertusingipaddress("192.168.100.1")
