def getipaddressconfig(routername):
    intconfig=""
    sampletemplate="""
    interface f0/0
     ip address ipinfof0/0
    interface f1/0
     ip address ipinfof1/0
    interface f0/1
     ip address ipinfof0/1
    """
    if (routername == "testindia"):
        f0_0="11.0.0.1 255.0.0.0"
        f1_0="10.0.0.1 255.0.0.0"
        sampletemplate=sampletemplate.replace("ipinfof0/0",f0_0)
        sampletemplate=sampletemplate.replace("ipinfof1/0",f1_0)
        sampletemplate=sampletemplate.replace("interface f0/1\n","")
        sampletemplate=sampletemplate.replace("ip address ipinfof0/1\n","")
    if (routername == "testusa"):
        f0_0="11.0.0.1 255.0.0.0"
        f0_1="12.0.0.1 255.0.0.0"
        sampletemplate=sampletemplate.replace("ipinfof0/0",f0_0)
        sampletemplate=sampletemplate.replace("ipinfof0/1",f0_1)
        sampletemplate=sampletemplate.replace("interface f1/0\n","")
        sampletemplate=sampletemplate.replace("ip address ipinfof1/0\n","")
    if (routername == "testUK"):
        f0_0="11.0.0.2 255.0.0.0"
        f0_1="12.0.0.2 255.0.0.0"
        sampletemplate=sampletemplate.replace("ipinfof0/0",f0_0)
        sampletemplate=sampletemplate.replace("ipinfof0/1",f0_1)
        sampletemplate=sampletemplate.replace("interface f1/0\n","")
        sampletemplate=sampletemplate.replace("ip address ipinfof1/0\n","")
    return sampletemplate

#calling this function
myfinaloutput=getipaddressconfig("testUK") #for UK router
myfinaloutput=getipaddressconfig("testindia") #for USA router
myfinaloutput=getipaddressconfig("testusa") #for India router
