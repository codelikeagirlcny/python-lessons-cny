import json

with open ('../contacts.json', 'r') as contacts_file:
    contacts = contacts_file.read()

print "contacts as a string: \n"
print contacts
print "\n\n"

contacts = json.loads(contacts)
print contacts

#print type(contacts[0])
contacts = contacts[0]  # to get rid of the list container
print type(contacts)
