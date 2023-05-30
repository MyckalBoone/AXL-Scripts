# Administartive XML SOAP API

# Update and Retrieve Client Details using zeep library

from zeep import Client
from zep.cache import SqliteCache
from zeep.transports import Transport
from requests import Session
from requests import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


USERNAME = input('Enter Admin username: ')
PASSWORD = getpass()
IP_ADDRESS = input('Enter the IP Address: ')

WSDL = 'schema//12.0//AXLAPI.wsdl'
BINDING_NAME = "{http://www.cisco.com/AXLAPIService/} AXLAPIBinding"
ADDRESS = "https://{ip}:8443/axl/".format(IP_ADDRESS)

def update_phone_by_name(client, name, description):
    '''update phone by name'''
    return client.updatePhone(**{'name': name, 'description': description})


def get_phone_by_name(client, name):
    '''Get Phone by Name'''
    return client.getPhone(name=name)

def main():
    '''Main'''
    session = session()
    session.verify = False
    session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
    transport = Transport(cache=SqliteCache(), session=session, timeout=60)
    client = Client(wsdl=WSDL, transport=transport)
    axl = client.create_service(BINDING_NAME, ADDRESS)

    update_phone_by_name(axl, "SEP001122334455", "DevAsc: adding new Desc")
    print(get_phone_by_name(axl, "SEP001122334455"))

if __name__=='__main__':
    main()
