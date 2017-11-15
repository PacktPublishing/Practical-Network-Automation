from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def validateinterface(ip):
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget((ip, 161)),
        0,25,
        '1.3.6.1.2.1.2.2.1.2',
        '1.3.6.1.2.1.2.2.1.7'
    )
    flag=False
    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                )
            )
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    if ("FastEthernet0/0" in val.prettyPrint()):
                        flag=True
    if (flag):
        return True
    else:
        return False

def finddevice(ip):
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
            if ("Cisco" in varBind.prettyPrint()):
                return True
    return False
 
mybyoddevices="192.168.255.249,192.168.255.248"
mybyoddevices=mybyoddevices.split(",")
for ip in mybyoddevices:
    getvendorvalidation=False
    getipvalidation=False
    print ("Validating IP",ip)
    getipvalidation=validateinterface(ip)
    print ("Interface has fastethernet0/0 :",getipvalidation)
    getvendorvalidation=finddevice(ip)
    print ("Device is of vendor Cisco:",getvendorvalidation)
    if getipvalidation and getvendorvalidation:
        print ("Device "+ip+" has passed all validations and eligible for BYOD")
        print ("\n\n")
    else:
        print ("Device "+ip+" has failed validations and NOT eligible for BYOD")
        print ("\n\n")  
