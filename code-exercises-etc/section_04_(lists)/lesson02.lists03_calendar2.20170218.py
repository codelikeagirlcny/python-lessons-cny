days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#print days_of_week

##for day in days_of_week:
##    print day


months_in_year = ['January', 'February']
months_in_year.extend(['March', 'April', 'May', 'June', 'July'])
months_in_year.extend(['August', 'September', 'October', 'November', 'December'])

for month in months_in_year:
    print month

    for week in range(1, 5): # [1, 2, 3, 4]
        print "Week {0}".format(week)

        for day in days_of_week:
            print day
