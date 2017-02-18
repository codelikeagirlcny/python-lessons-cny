##things = []
##print things

attendees = ['Alison', 'Belen', 'Rebecca', 'Nura']
#print attendees

print attendees[0]

##name = 'Alison'
##print name[0]

print attendees[1:3]
print attendees[:3]

#print attendees[4]

#print len(attendees)
number_of_attendees = len(attendees)
print number_of_attendees

attendees.append("Andrea")
print attendees

##print "\n\n\n"

## oh by the way, our list can contain a mix of strings and numbers!
##attendees.append(4)
##print attendees

## change the first peron's name to be spelled wrong
##print attendees[0]
##attendees[0] = "Allison"
##print attendees

attendees.insert(2, "Samantha")
print attendees

#### a list of numbers! just to see it a different way ####
attendees_ages = []
print attendees_ages
print len(attendees_ages)

attendees_ages.append(28)
print attendees_ages
print len(attendees_ages)

attendees_ages.append(27)
print attendees_ages
print len(attendees_ages)

attendees_ages[0] = attendees_ages[0] + 1
print attendees_ages
