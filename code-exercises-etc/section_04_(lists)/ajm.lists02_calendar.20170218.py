days_of_week = ['Monday', 'Tuesday']
print days_of_week

days_of_week.append('Wednesday')
print days_of_week

days_of_week.append('Thursday')
print days_of_week

days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')
print days_of_week
print len(days_of_week)

print "\n\n"

last_day_in_week = days_of_week.pop()
print last_day_in_week
print days_of_week

print "\n\n"

fourth_day_in_week = days_of_week.pop(3)
print fourth_day_in_week
# print "here is the fourth day", fourth_day_in_week
print days_of_week
print len(days_of_week)


print "\n\n...and now, months!\n"

months = ['January', 'February']
print months

##months.append(['March', 'April'])
##print months
months.extend(['March', 'April', 'May', 'June', 'July'])
months.extend(['August', 'September', 'October', 'November', 'December'])
print months
print len(months)

months.pop(0)
print months

months.insert(0, 'January')
print months
