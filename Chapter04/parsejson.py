import requests
r = requests.get('https://github.com/timeline.json')
jsonvalue=r.json()
print (jsonvalue)
print ("\nNow printing value of message"+"\n")
print (jsonvalue['message']+"\n")
