import cgi

form = cgi.FieldStorage()
value=int(form.getvalue('number'))
callername=form.getvalue('name')

print('Content-Type: text/html')
print('')
xval=0
tval="<h2>Hello <font color='red'>"+callername+"</font><h2><br><h3>Your requested output is below:</h3>"
tval=tval+"<table border='1' style='border-collapse: collapse'><tr><th>Table for "+str(value)+"</th></tr>"
for xval in range(1,11):
    mval=value*xval
    tval=tval+"<tr><td>"+str(value)+"</td><td>*</td><td>"+str(xval)+"</td><td>=</td><td><font color='blue'><b>"+str(mval)+"</b></font></td></tr>"

tval=tval+"</table>"

print(tval)
