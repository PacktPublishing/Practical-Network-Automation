import re
sampletext="""
interface fa0/1
switchport mode trunk
no shut

interface fa0/0
no shut

interface fa1/0
switchport mode trunk
no shut

interface fa2/0
shut

interface fa2/1
switchport mode trunk
no shut

interface te3/1
switchport mode trunk
shut
"""

sampletext=sampletext.split("interface")
#check for interfaces that are in trunk mode
for chunk in sampletext:
    if ("mode trunk" in chunk):
        if ("no shut" in chunk):
            intname=re.search("(fa|te)\d+/\d+",chunk)
            print ("Trunk enabled on "+intname.group(0))
