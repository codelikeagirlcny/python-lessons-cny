days_of_week = ['Monday', 'Tuesday']

days_of_week.append('Wednesday')
##print days_of_week
##print len(days_of_week)

days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')

##print len(days_of_week)
print days_of_week
##
###day = days_of_week.pop()
##
##day = days_of_week.pop(3)
##
##print len(days_of_week)
##print days_of_week
##print day



months = ['January', 'February']
#months.append(['March', 'April', 'May'])
#months.append(5)

months.extend(['March', 'April', 'May'])
#print months

months_after_may = ['June', 'July', 'August', 'September', 'October', 'November', 'December']
months.extend(months_after_may)

print months

print '\n'

months.insert(3, 'Alisonmonth')
print months
