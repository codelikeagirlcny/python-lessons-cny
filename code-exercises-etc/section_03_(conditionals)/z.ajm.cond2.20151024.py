students = 70
capacity = 100

tas = 5

if students < capacity:
    print "Keep recruiting students!"
else:
    print "Close ticket signups!"


if tas == 0:
    print "No TAs -- uh oh!"
elif tas < students / 5:
    print "Keep recruiting TAs!"
else:
    print "All set on TAs -- aren't they great?"

print 5 == 5
