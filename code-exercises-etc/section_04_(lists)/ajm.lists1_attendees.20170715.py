##list_of_people = []
##person_name = ''

my_name = 'Alison'

attendees = ['Alison', 'Carolyn', 'Hannah']
print attendees
#print attendees[0]
#print my_name[0]

print len(attendees)
#print len(my_name)

attendees.append('Alyssa')
print attendees
print len(attendees)

attendee_ages = [35, 25, 41, 19]
print attendee_ages

##fruit1 = "apple"
##fruit2 = "banana"
##fruit3 = "pear"
##fruits = [fruit1, fruit2, fruit3]
##
##num_attend_july15 = 6
##num_attend_july01 = 4
##num_attend_aug04 = 7
##attendance = [num_attend_july15, num_attend_july01, num_attend_aug04]
##

attendees[2] = "Hanna"
print attendees

print "\n\n\n\n\n"



days_of_week = ["Monday", 'Tuesday']
#print days_of_week
#print len(days_of_week)
days_of_week.append('Wednesday')
#print days_of_week
#print len(days_of_week)
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')
print days_of_week

#days_of_week.pop()
day = days_of_week.pop()
print days_of_week
print day
days_of_week.append(day)
print days_of_week

print "\n\n\n\n\n"

#day = days_of_week.pop(3)
#print day

months = ['January', 'February']
months.append('March')
print months
#months.append(['April','May','June'])
#print months
months.extend(['April', 'May','June','July','August','September'])
months.extend(['October', 'November', 'December'])
print '\n'
print months
print len(months)

print "\n\n\n\n\n"

months.pop(2)
#second_month = months.pop(2)
print months
months.insert(2, 'March')
#months.insert(2, second_month)
print months

print "\n\n\n\n\n"

address = '654 E Street SE Washington DC 20003'
print address
address_as_list = address.split(" ")
print address_as_list

print "\n\n\n\n\n"

print attendees
print my_name

if 'son' in my_name:
    print "'son' is in the my_name string."
else:
    print "'son' is not in the my_name string."

if 'son' in attendees:
    print "'son' is in the attendees list."
else:
    print "'son' is not in the attendees list."




















































