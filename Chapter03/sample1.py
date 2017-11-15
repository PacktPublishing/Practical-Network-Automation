ipdict={'india': '1.1.1.1,1.1.1.2', 'uk': '3.1.1.1,3.1.1.2', 'usa': '2.1.1.1,2.1.1.2'}

standardtemplate="""
hostname <hname>
ip domain-lookup
ip name-server <nameserver>
logging host <loghost>
username cisco privilege 15 password cisco
enable password cisco
ip domain-name checkmetest.router

line vty 0 4
 exec-timeout 5
"""

routerlist="R1,R2,R3"
routers=routerlist.split(",")
for router in routers:
print ("Now printing config for",router)
    if "R1" in router:
        hostname="testindia"
        getips=ipdict["india"]
        getips=getips.split(",")
        logserver=getips[0]
        nameserver=getips[1]
    if "R2" in router:
        hostname="testusa"
        getips=ipdict["usa"]
        getips=getips.split(",")
        logserver=getips[0]
        nameserver=getips[1]
    if "R3" in router:
        hostname="testUK"
        getips=ipdict["uk"]
        getips=getips.split(",")
        logserver=getips[0]
        nameserver=getips[1]
    generatedconfig=standardtemplate
    generatedconfig=generatedconfig.replace("<hname>",hostname)
    generatedconfig=generatedconfig.replace("<nameserver>",nameserver)
    generatedconfig=generatedconfig.replace("<loghost>",logserver)
    print (generatedconfig)
