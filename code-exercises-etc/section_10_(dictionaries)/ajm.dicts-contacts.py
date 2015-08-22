## Exercise started with ./dict_exercise_2.py, but incorporats a few others in this dir
contacts = {
    'Alison': {
        'phone':'315-481-2904',
        'twitter':'@alisonjo2786',
        'github':'alisonjo2786'
    },
    'Shannon': {
        'phone':'202-555-1234',
        'twitter':'@svt',
        'github':'shannonturner'
    },
    'Brigid': {
        'phone' : '315-555-9876',
        'twitter' : '@therealbrigid',
        'github' : 'brigidongithub'
    }
}
#print contacts

contacts['Nina'] = {
    'phone': '301-555-1234',
    'github': 'ninaGH'
}
#print contacts

#list_of_contacts_keys = contacts.keys()
#for contact in sorted(list_of_contacts_keys):

for contact in sorted(contacts.keys()):
    print '{0}\'s info:'.format(contact)
    for contact_type in contacts[contact].keys():
        print '\t{0}: {1}'.format(contact_type, contacts[contact][contact_type])

#print contacts.items()
#print contacts.get('Alison').items()



