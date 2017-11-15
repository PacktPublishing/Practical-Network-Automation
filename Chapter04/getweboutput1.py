import cgi
from netmiko import ConnectHandler
import time

form = cgi.FieldStorage()
ipvalue=form.getvalue('ipaddress')

def getoutput(cmd):
    global ipvalue
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=ipvalue, username=uname, password=passwd)
    output=device.send_command(cmd)
    return (output)

print('Content-Type: text/plain')
print('')
print ("Device queried for ",ipvalue)
print ("\nOutput:")
print (getoutput("show version"))
