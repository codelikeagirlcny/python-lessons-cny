days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months_in_year = ['January', 'February', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

##for leaf in days_of_week:
##    print leaf
##    # leaf = 'Monday'
##    # print leaf
##    #
##    # leaf = 'Tuesday'
##    # print leaf
##    #
##    # etc.

# part 1...
for day in days_of_week:
    print day
for week_number in range(1, 5): #[1, 2, 3, 4]
    print 'Week {0}'.format(week_number)

# part 2...
for week_number in range(1, 5): #[1, 2, 3, 4]
    print '\nWeek {0}'.format(week_number)
    for day in days_of_week:
        print day

# part 3...
for month in months_in_year:
    print '\n{0}'.format(month)
    for week in range(1, 5):
        print 'Week {0}'.format(week)
        # or, extra fancy:
        # print '\tWeek {0}'.format(week)
        for day in days_of_week:
            print day
            # or, extra fancy:
            # print '\t\t{0}'.format(day)
