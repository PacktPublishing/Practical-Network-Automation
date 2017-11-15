print('Content-Type: text/html')
print('')
value=5
xval=0
tval="<table border='1' style='border-collapse: collapse'><tr><th>Table for "+str(value)+"</th></tr>"
for xval in range(1,11):
    mval=value*xval
    tval=tval+"<tr><td>"+str(value)+"</td><td>*</td><td>"+str(xval)+"</td><td>=</td><td><font color='blue'><b>"+str(mval)+"</b></font></td></tr>"

tval=tval+"</table>"

print(tval)
