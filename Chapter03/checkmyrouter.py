from netmiko import ConnectHandler
import time

uname="cisco"
passwd="cisco"
device = ConnectHandler(device_type='cisco_ios', ip="192.168.255.249", username=uname, password=passwd)
output=device.send_command("show run | in boot")
print ("Current config:")
print (output)
cmd="boot system flash:c3745-adventerprisek9-mz.124-15.T14.bin"
device.send_config_set(cmd)
print ("New config:")
output=device.send_command("show run | in boot")
print (output)
device.send_command("wr mem")
device.disconnect()
