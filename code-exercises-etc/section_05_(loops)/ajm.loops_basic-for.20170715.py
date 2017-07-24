attendees = ['Alison', 'Carolyn', 'Hannah']

for person in attendees: #for "name of variable that we're going to use as we go through this list" in "this list"
    print person
    #person = 'Alison', print person
    #person = 'Carolyn', print person

for cow in range(5):
    print cow

print '\n\n\n\n\n'

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_week:
    print day

##print days_of_week[0]
##print days_of_week[1]
##print days_of_week[2]

for week in range(1,5): #[1,2,3,4]
    print "Week {0}".format(week)


print '\n\n\n\n\n'


##for week in range(1,5): #[1,2,3,4]
##    print "Week {0}".format(week)
##    for day in days_of_week:
##        print day

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

##for cake in months:
##    print '\n'
##    print cake
##
##    for week in range(1,5): #[1,2,3,4]
##        print "\tWeek {0}".format(week)
##
##        for day in days_of_week:
##            print "\t\t", day


print '\n\n\n\n\n'

for index, day in enumerate(days_of_week): #or, for dog, day in ...
    print "Day {0}: {1}".format(index + 1, day)





























