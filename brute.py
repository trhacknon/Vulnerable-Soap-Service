from suds.client import Client
client = Client('http://127.0.0.1:8000/?wsdl')
print(client)
username_list=["admin","test","siber","siber1"]
for username in username_list:
	print(client.service.query(username))
