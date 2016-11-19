contacts = {
    'Shannon' : {'phone' : '202-555-1234',
                 'twitter' : '@svt827',
                 'github' : 'shannonvturner'
                 },
    'Bridgit' : {'phone' : '703-555-1222',
                 'github' : 'bridgitongithub'
                 },
    'Alison' : {'phone' : '315-555-1111',
                'twitter' : '@alisonjo2786',
                'github' : 'alisonjo2786'
                }
}

for contact in contacts.keys():
    print contact
    #print contacts.get(contact)
    #print contacts.get(contact).get('twitter')

for contact in sorted(contacts.keys()):
    print contact

for info in contacts.values():
    print info

for contact, info in contacts.items():
    #print contact, info
    print "{0}:".format(contact)

    for info_key,info_val in info.items():
        print "\t{0}: {1}".format(info_key,info_val)
