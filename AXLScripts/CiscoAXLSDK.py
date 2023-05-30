# pip3 install ciscoaxl

from ciscoaxl import axl

CUCM = input('Enter CUCM: ')
CUCM_USER = input('Enter your CUCM user: ')
CUCM_PASSWORD = getpass()
CUCM_VERSION = input('Enter the CUCM version: ')

ucm = axl(username=CUCM_USER,password=CUCM_PASSWORD,cucm=CUCM,version=CUCM_VERSION)
print (ucm)

for phone in ucm.get_phones():
    print (phone.name)

for user in ucm.get_users()
    print (user.firstName)
