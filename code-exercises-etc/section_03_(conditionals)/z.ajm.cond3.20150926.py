volunteers = 10
goal = 50

if volunteers < goal:
    print "More volunteers are needed."
    print "{0} more volunteers are needed.".format(goal-volunteers)
elif volunteers == goal:
    print "We have enough volunteers."
elif volunteers > goal:
    print "We have a volunteer surplus."
else:
    print "This is unexpected......"
