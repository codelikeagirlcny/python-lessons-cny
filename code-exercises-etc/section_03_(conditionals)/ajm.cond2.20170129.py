## in-class exercise -- multiple ways of doing it, from different people



volunteers = 90
goal = 100

if volunteers > goal:
    print "overachiever!"
elif volunteers < goal:
    print "slacker!"
elif volunteers == goal:
    print "good enough!"
else:
    print "Stuff's getting weird."






volunteers = 90
goal = 100

if volunteers < goal:
    print "You're behind!"

if volunteers == goal:
    print "Good job!"
elif volunteers < goal:
    print "You're behind!"
elif volunteers >= goal:
    print "You exceeded the goal!"

## if volunteers >= 5 x goal and [etc]

if volunteers == goal:
    print "Congrats!"
elif volunteers > goal:
    print "You've exceeded goal by {0}!".format(volunteers - goal)
else:
    print "You are behind on your goal by {0}.".format(goal - volunteers)
