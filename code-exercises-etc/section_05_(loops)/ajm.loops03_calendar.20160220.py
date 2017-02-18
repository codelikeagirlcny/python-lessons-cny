days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

##for day in days_of_week:
##    print day

for month in months:
    print month
    
    for week in range(1, 5):
        print 'Week {0}'.format(week)

        for day in days_of_week:
            print day

    print '\n'

