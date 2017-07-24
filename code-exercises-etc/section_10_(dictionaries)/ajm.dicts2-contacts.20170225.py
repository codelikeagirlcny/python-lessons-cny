#empty list
#people = []

#empty dict
#contacts = {}

contacts = {
    "Alison" : "315-481-2904",
    "Belen" : "315-555-9876",
    "Rebecca" : "315-555-1234"
    }

#print people[0]
print contacts['Alison'] # 315-481-2904

contacts['Jamie'] = '315-555-6543'
#contacts['Alison'] = '315-481-2409'

#print contacts['Frankenstein'] -> produces KeyError
## Instead, use .get() dict method...
print contacts.get('Frankenstein')

##Also...
#print contacts.get('Frankenstein', 'No one with that name')







