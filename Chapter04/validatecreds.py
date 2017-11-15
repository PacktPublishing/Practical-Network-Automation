import cgi, cgitb
import requests
from requests.auth import HTTPBasicAuth

form = cgi.FieldStorage()
uname=form.getvalue('name')
password=form.getvalue('password')

r = requests.get('http://localhost/apitest/api/apitest/5', auth=(uname, password))

print('Content-Type: text/HTML')
print('')
print ("<h2>Hello "+uname+"</h2>")

htmlform="<form action='showoutput.py' method='post'>"
htmlform=htmlform+"<br><input type='radio' name='ipaddress' value='192.168.255.248' /> 192.168.255.248"
htmlform=htmlform+"<br><input type='radio' name='ipaddress' value='192.168.255.249' /> 192.168.255.249"
htmlform=htmlform+"<br><input type='submit' value='Select IPaddress' /></form>"

if (r.status_code != 200):
    print ("<h3><font color='red'>Not Authorized.</font> Try again!!!!</h3>")
else:
    print ("<h3><font color='lime'>Authorized.</font> Please select from list below:</h3>")
    print (htmlform)
