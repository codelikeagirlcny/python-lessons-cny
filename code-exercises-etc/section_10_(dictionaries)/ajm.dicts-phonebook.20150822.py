phonebook_as_list = [
    ['Alison','315-481-2904'],
    ['Shannon','202-555-1234'],
    ['Brigid','315-555-9876']
]

#loop, probably with enumerate...
#conditional asking something like
# if phonebook[index][0] == 'Shannon' tell me what
# phonebook[index][1] is.

phonebook_as_dictionary = {
    'Alison':'315-481-2904',
    'Shannon':'202-555-1234',
    'Brigid':'315-555-9876'
}
#print phonebook_as_dictionary['Shannon']
#print phonebook_as_list[1][1]

phonebook_as_dictionary['Mel'] = '301-555-4569'
print phonebook_as_dictionary

#compare...
#print phonebook_as_dictionary['Frankenstein']
#versus...
#print phonebook_as_dictionary.get('Frankenstein')
#versus...
#print phonebook_as_dictionary.get('Frankenstein', 'Cannot find anything with that name!')
