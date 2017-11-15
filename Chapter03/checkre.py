import re
mystring='My ip address is 10.10.10.20 and by subnet mask is 255.255.255.255'

if (re.search("ip address",mystring)):
    ipaddregex=re.search("ip address is \d+.\d+.\d+.\d+",mystring)
    ipaddregex=ipaddregex.group(0)
    ipaddress=ipaddregex.replace("ip address is ","")
    print ("IP address is :",ipaddress)

if (re.search("subnet mask",mystring)):
    ipaddregex=re.search("subnet mask is \d+.\d+.\d+.\d+",mystring)
    ipaddregex=ipaddregex.group(0)
    ipaddress=ipaddregex.replace("subnet mask is ","")
    print ("Subnet mask is :",ipaddress)
