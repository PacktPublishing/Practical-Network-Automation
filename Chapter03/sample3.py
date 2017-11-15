from netmiko import ConnectHandler
import time


def pushimage(imagename,cmd,myip,imgsize,md5sum=None):
    uname="cisco"
    passwd="cisco"
    print ("Now working on IP address: ",myip)
    device = ConnectHandler(device_type='cisco_ios', ip=myip, username=uname, password=passwd)
    outputx=device.send_command("dir | in Directory")
    outputx=outputx.split(" ")
    outputx=outputx[-1]
    outputx=outputx.replace("/","")
    precmds="file prompt quiet"
    postcmds="file prompt"
    xcheck=device.send_config_set(precmds)
    output = device.send_command_timing(cmd)
    flag=True
    devicex = ConnectHandler(device_type='cisco_ios', ip=myip, username=uname, password=passwd)
    outputx=devicex.send_command("dir")
    print (outputx)
    while (flag):
        time.sleep(30)
        outputx=devicex.send_command("dir | in "+imagename)
        print (outputx)
        if imgsize in outputx:
            print("Image copied with given size. Now validating md5")
            flag=False
        else:
            print (outputx)
        if (flag == False):
            cmd="verify /md5 "+imagename
            outputmd5=devicex.send_command(cmd,delay_factor=50)
        if (md5sum not in outputmd5):
            globalflag=True
            print ("Image copied but Md5 validation failed on ",myip)
        else:
            print ("Image copied and validated on ",myip)
    devicex.send_config_set(postcmds)
    devicex.disconnect()
    device.disconnect()
    

ipaddress="192.168.255.249"
imgname="c3745-adventerprisek9-mz.124-15.T14.bin"
imgsize="46509636"
md5sum="a696619869a972ec3a27742d38031b6a"
cmd="copy ftp://ftpuser:ftpuser@192.168.255.250/c3745-adventerprisek9-mz.124-15.T14.bin flash:"
pushimage(imgname,cmd,ipaddress,imgsize,md5sum)
