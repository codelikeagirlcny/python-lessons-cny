twitter = "@alisonjo2786"

#print len(twitter)


print twitter[0]
print twitter[6]
print twitter[12]


print "\n\n"

print twitter[1:5]

print twitter[1:99]



phone = '(315) 555-1234'
# 315
# 555
print phone[1:4]
print phone[6:9]


print "\n\n"


tweet = "In just over one year, @hearmecode has reached over 800 members who are learning how to code together."

print """That tweet is {0} characters.
You have {1} characters left.""".format(len(tweet), 140-len(tweet))

print "\n\n"


phone = '315-555-1234'
print "For great pizza, call {0}.".format(phone[4:])

print "\n\n"




print "Area code: {0}".format(phone[:3])
print "Local: {0}".format(phone[4:])
print "Different format: ({0}) {1}".format(phone[:3], phone[4:])
print "\n\n"

#print "Some things: {0}".format(phone.replace("-", " "))
#modified_phone = phone.replace("-", " ")
