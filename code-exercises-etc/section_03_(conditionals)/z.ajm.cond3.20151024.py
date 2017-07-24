volunteers = 10
goal = 50

##if volunteers < goal:
##    print "More volunteers are needed."
##    print "{0} more volunteers are needed.".format(goal-volunteers)
##elif volunteers == goal:
##    print "We have enough volunteers."
##elif volunteers > goal:
##    print "We have a volunteer surplus."
##else:
##    print "This is unexpected......"

if volunteers < goal:
    print "You are {0} below your goal".format(goal - volunteers)
elif volunteers == goal:
    print "At your goal"
elif volunteers > goal:
    print "You're above your goal"
else:
    print "er, something weird happened"
