from http.client import HTTPConnection
connection= HTTPConnection("bridgelabz.com")
connection.request("GET","/")
output=connection.getresponse()
contents= output.read()
print(contents)











