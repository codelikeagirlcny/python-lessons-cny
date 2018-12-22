students = 10
capacity = 50

if students < capacity:
    print "Keep recruiting"
else:
    print "end ticket signups"

students = 50
capacity = 50

if students > capacity:
    print "end ticket signups"
else:
    print "keep recruiting"

#else does NOT get a conditional
#else is a fallback/catch-all/backup
#if students < capacity:
#    print "keep recruiting"
#else students >= capacity:
#    print "end ticket signups"

tas = 5

if tas == 0:
    print "None? uh oh!"
    # send another desperate plea for TAs
elif tas < students / 5:
    print "keep recruiting tas"
    # wait another few days, check signups
else:
    print "we have all the tas we need, yay!"
    # close TA signup form

# ^^ use code comments to tell yourself an outline
# of what you intend to do

volunteers = 10
goal = 20

if volunteers < goal:
    print "you need more volunteers"
    # print "you still need ___ volunteers"
else:
    print "you have enough volunteers!"

email = "alisonjo2786@gmail.com"
if "alisonjo2786@gmail.com".count("@") > 1:
    # return an email validation error
    print "you did it wrong"


# COMPOUND CONDITIONALS

if students < capacity and tas < students/5:
    print "woah we are terrible at recruiting"

gender = "f"
if gender.lower() != "f" and students < capacity:
    # let the boys in
else:
    print "no boys allowed"

if gender.lower() == "f" or students < capacity:
    # let the boys in
else:
    # no boys allowed

days_left = 3
if students >= capacity:
    # no more humans
else:
    if days_left < 4:
        # let the boys in
    elif days_left >= 4:
        # offer wait list spot
    else:
        # wait, what?
