volunteers = 90
goal = 100

##if volunteers >= goal:
##    print "You did it!"
##elif volunteers == goal:
##    print "Right on!"

##if volunteers == 0 and goal == 0:
##    # er, what?
##else:
if volunteers == goal:
    print "You're at the goal, awesome!"
elif volunteers > goal:
    print "Oooo somebody's an overachiever."
elif volunteers < goal:
    print "You still have some work to do."
else:
    print "Not sure what happened, but somehow volunteers is not equal to, greater than, or less than goal..."

print "\n"

# "extra credit"
if volunteers == goal:
    print "You're at the goal, awesome!"
elif volunteers > goal:
    print "Oooo somebody's an overachiever -- you have {0} more volunteers than you need.".format(volunteers - goal)
elif volunteers < goal:
    print "You still need {0} more volunteers.".format(goal - volunteers)
else:
    print "Not sure what happened, but somehow volunteers is not equal to, greater than, or less than goal... volunteers is {0}, goal is {1} ".format(volunteers, goal)


###compound conditionals
##if men_quoted == 0 and women_quoted == 0:
##    # do stuff
##
##if men_quoted == 0:
##    if women_quoted == 0:
##        # do stuff









