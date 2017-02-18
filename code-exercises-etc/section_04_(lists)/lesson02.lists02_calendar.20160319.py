print 'here are day things...'

days_of_week = ['Monday', 'Tuesday']

days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')

print days_of_week
print len(days_of_week)

print '\nhere come month things...'

months = ['January', 'February']
months.append('March')
month9 = 'September'
month10 = 'October'
months.extend(['April', 'May','June',"July","August"])
months.append(month9)
months.extend([month10, 'November', 'December'])

print months
print len(months)

print months.pop(1)
