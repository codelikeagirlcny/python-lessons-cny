contact_list = {
    "Hear Me Code": {
      "twitter": "@hearmecode",
      "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
      "twitter": "@svt827",
      "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contact_list["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!
contact_list['Alison McCauley'] = {
    'twitter' : '@alisonjo2786',
    'github' : 'https://github.com/alisonjo2786'
}
contact_list['Kristen Link'] = {
    'github' : 'https://github.com/kristenongithub'
}
contact_list['Sarah Roche'] = {
    'github' : 'https://github.com/sarahongithub',
    'twitter' : '@sarahroche'
}
contact_list['Dee Cater'] = {
    'twitter' : '@deecater',
    'github' : 'https://github.com/deeongithub'
}
contact_list['Nina Verity'] = {
    'twitter' : '@ninaverity',
    'github' : 'https://github.com/githubninav'
}

#print contact_list
#print contact_list.keys()

for contact_key in contact_list.keys():
    print contact_list.get(contact_key)

print '\n\n'

#now sorted alphabetically
for contact_key in sorted(contact_list.keys()):
    print contact_list.get(contact_key).get('twitter')

#now looping through the nested dictionary
for key, value in contact_list.items():
    print key, '\t', value

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:
# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner
for key, value in contact_list.items():
    print '{0}\'s info:'.format(key)
    print '\ttwitter:', contact_list.get(key).get('twitter')
    print '\tgithub:', contact_list.get(key).get('github')
