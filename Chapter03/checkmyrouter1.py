from netmiko import ConnectHandler
import time

def getoutput(cmd):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip="192.168.255.249", username=uname, password=passwd)
    output=device.send_command(cmd)
    return (output)


checkprepost=input("Do you want a pre or post check [pre|post]: ")
checkprepost=checkprepost.lower()
if ("pre" in checkprepost ):
    fname="precheck.txt"
else:
    fname="postcheck.txt"

file=open(fname,"w")
file.write(getoutput("show ip route"))
file.write("\n")
file.write(getoutput("show clock"))
file.write("\n")
file.write(getoutput("show ip int brief"))
file.write("\n")

print ("File write completed",fname)

file.close()
