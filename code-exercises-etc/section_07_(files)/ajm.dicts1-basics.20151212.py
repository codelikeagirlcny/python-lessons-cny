#without dictionaries...
##people_on_github = [['Alison', 'alisonjo2786'], ['Dee', 'deeongithub'], ['Sarah', 'Sarahongithub']]
##print people_on_github[0][1]
##for person in people_on_github:
##    if person[0] == 'Alison':
##        print person[1]

#with dictionaries...
people_on_github = {
    'Alison' : 'alisonjo2786',
    'Dee' : 'deeongithub',
    'Sarah' : 'Sarahongithub'
}

print people_on_github['Alison']
