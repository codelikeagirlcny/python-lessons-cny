gender = 'm'

if gender == 'f':
    print "welcome!"

print "\n\n"

students = 10
capacity = 50

if students < capacity:
    print "Keep recruiting!"
    # and on
    # and on
else:
    print "End ticket signups."
    # and on
    # and on


print "\n\n"


TAs = 0

if TAs == 0:
    print "uh oh..."
elif TAs < students / 5:
    print "Keep recruiting TAs"
##elif TAs >= students / 5:
##    print "We have enough TAs."
else:
    print "We're good on TAs."
    #print "Um not sure what is going on with math."

print "\n\n"


vols = 10
goal = 100
if vols == goal:
    print "You've reached the vol goal!"
elif vols < goal:
    print "You are behind the vol goal."
else:
    print "You're most likely over the vol goal!"


print "\n\n"

gender = 'F'
email = "alisonjo2786@gmail.com"

if gender.lower() == 'f':
    print "welcome"

if email.count("@") > 1:
    print "email address not valid"


print "\n\n"

if type(email.find("@")) == int and email.count("@") == 1:
    print "good job with the email address"

if email.count("@") > 1 or email.count("@") < 1:
    print "bad job with the email address"


print "\n\n"

if type(vols) == int and type(goal) == int:
    if vols == goal:
        print "You've reached the vol goal!"
    elif vols < goal:
        print "You are behind the vol goal."
    else:
        print "You're most likely over the vol goal!"
else:
    print "vols and/or goal are not integers"

if email.count("@") > 1 or email.count("@") < 1:
    print "email address not valid"
else:
    #test for other stuff that proves valid email...
    #if something: do stuff











