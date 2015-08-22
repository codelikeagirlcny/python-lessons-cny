days_of_workweek = ['Monday','Tuesday']
#print days_of_workweek

days_of_workweek.append('Wednesday')

days_of_workweek.extend(['Friday', 'Saturday', 'Sunday'])
#print days_of_workweek

days_of_workweek.insert(3, 'Thursday')
print days_of_workweek

third_day = days_of_workweek.pop(2)

print third_day
print days_of_workweek
