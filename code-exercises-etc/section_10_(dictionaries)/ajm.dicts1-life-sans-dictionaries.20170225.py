#Without dictionaries...
#If I want to grab a twitter handle and I have a nested list of people & contact info...
people = [
    ['Alison','@alisonjo2786','315-481-2904'],
    ['Rebecca','@rebeccaontwitter','315-555-1234'],
    ['Belen','@belenbelen','315-555-9876']
    ]

for person in people:
    if person[0] == 'Alison':
        print person[1]
