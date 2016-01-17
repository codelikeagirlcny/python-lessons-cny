contact_list = {
    'Alison' : '315-481-2904',
    'Dee' : '315-555-9876',
    'Sarah' : '315-555-4567'
}

#add to a dictionary
contact_list['Andrea'] = '315-555-4646'
#print contact_list

#print contact_list['Alison']

#print contact_list['Kristen']
print contact_list.get('Kristen')

print contact_list.get('Kristen', 'No one here')
