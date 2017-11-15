from pysnmp.hlapi import *

print('Content-Type: text/html')
print('')

def finddevices(ip):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            xval=(' = '.join([x.prettyPrint() for x in varBind]))
            xval=xval.replace("SNMPv2-MIB::sysDescr.0 = ","")
            xval=xval.split(",")
            return (xval[1])

ipaddress="192.168.255.248,192.168.255.249"
ipaddress=ipaddress.split(",")
tval="<table border='1'><tr><td>IP address</td><td>Model</td></tr>"
for ip in ipaddress:
    version=finddevices(ip)
    version=version.strip()
    ahref="http://localhost/test/showversion.py?ipaddress="+ip
    tval=tval+"<tr><td><a href='"+ahref+"' target='_blank'>"+ip+"</a></td>"
    
    tval=tval+"<td>"+version+"</td></tr>"

tval=tval+"</table>"
print (tval)   
