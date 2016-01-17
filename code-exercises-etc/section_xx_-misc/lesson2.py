days_of_week = ['Monday', 'Tuesday']
days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')
#print days_of_week
#print len(days_of_week)
day = days_of_week.pop(3)
#print day
#print days_of_week
#print len(days_of_week)
months = ['January', 'February']
months.extend(['March', 'April','May','June'])
#print months
months_second_half = ['July','August','September','October','November','December']
months.extend(months_second_half)
#print months
days_of_week.insert(3, 'Thursday')
print days_of_week
days_of_week.remove('Thursday')
print days_of_week
