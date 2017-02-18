days_of_week = ['Monday', 'Tuesday']

days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')

months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months_in_year:
    print month

    for week in range(1,5): # [1, 2, 3, 4]
        print "Week {0}".format(week)

        for day in days_of_week:
            print day
