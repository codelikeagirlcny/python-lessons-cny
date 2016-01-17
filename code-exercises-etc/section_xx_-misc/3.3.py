contacts = {}

contacts = {
    'Shannon':'202-555-1234',
    'Bridgit':'703-555-9876',
    'Christine':'410-555-3048'
}

#reading part of a string
#name[0:5] #outputs Shann
#reading part of a list
#attendees[:3] #outputs Amy, Jen, Julie

#reading part of a dictionary
contacts['Shannon'] #202-555-1234

#adding to a dictionary
contacts['Mel'] = '301-333-1212'

#reading from a dictionary, the error-prone way
#print contacts['Frankenstein'] #returns a KeyError

#reading from a dictionary, the non-error-prone way!
#print contacts.get('Frankenstein') #returns te word None

attendees = {
    'Feb 1': ['Jen', 'Amy', 'Julie'],
    'Feb 2': ['Sarah', 'Chris', 'Jenna']
    }

contacts['Shannon'] = {
    'phone':'202-555-1234',
    'twitter':'@svt827',
    'github':'@shannonturner'
}

#print contacts['Shannon']['github']

#for contact in contacts:
#for contact in contacts.keys():
#for contact in sorted(contacts.keys()):
#    print contact
#    print contacts[contact]

#print contacts.keys()

#for contact_info in contacts.values():
#    print contact_info

#for contact,info in contacts.items():
#    print contact,info


contacts['Mel'] = {
    'phone':'232-454-676',
    'instagram':'@melontwitter',
    'github':'@melodykramer'
}
contacts['Bridgit'] = {
    'phone':'703-555-9876',
    'twitter':'@bridgitwithad',
    'tumblr':'@bridgitb'
}
contacts['Christine'] = {
    'phone':'410-555-3048',
    'twitter':'@christinetime',
    'github':'@ladychristine'
}

for contact,info in contacts.items():
    print '{0}\'s contact info is:'.format(contact)
    for info_k,info_v in info.items():
        print '\t{0}: {1}'.format(info_k,info_v)















