from netmiko import ConnectHandler

def takebackup(cmd,rname):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=rname, username=uname, password=passwd)
    output=device.send_command(cmd)
    fname=rname+".txt"
    file=open(fname,"w")
    file.write(output)
    file.close()


# assuming we have two routers in network 
devices="rtr1,rtr2"
devices=devices.split(",")

for device in devices:
    takebackup("show run",device)
