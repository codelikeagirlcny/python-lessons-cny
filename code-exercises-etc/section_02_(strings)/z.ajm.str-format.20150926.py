name = "Alison"
age = 29
#print "My name is {1} and my age is {0}.".format(name, age)


phone = "315-555-2955"
#print "Call {0} for great pizza!".format(phone[4:])

print """Area Code: {0}
Local: {1}
Different format: ({0}) {3}-{4}""".format(phone[:3], phone[4:], phone[:3], phone[4:7], phone[8:])


tweet = "Saying things that you really want to know"
length_of_tweet = len(tweet)

#print """That tweet is {0} characters.
#You have {1} characters left.""".format(len(tweet), 140-len(tweet))
