from suds.client import Client
client = Client('http://127.0.0.1:8000/?wsdl')
print(client)
print(client.service.get_admin_mail(""))
print(client.service.get_admin_mail("admin"))

