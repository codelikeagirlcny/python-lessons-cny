name = "Alison"
age = 31

##print "My name is"
##print name
##print "and my age is"
##print age

##print "My name is {0}, and my age is {1}.".format(name, age)
##print "My name is {1}, and my age is {0}.".format(name, age)


tweet = """I love my dinner, here is a picture!"""

##tweet_length = 99
##tweet_remaining = 41
##print """That tweet is {0} characters.
##You have {1} characters left.""".format(tweet_length, tweet_remaining)

print """That tweet is {0} characters.
You have {1} characters left.""".format(len(tweet), 140-len(tweet))

max_tweet_length = 140
tweet_length = len(tweet)
print """That tweet is {0} characters.
You have {1} characters left.""".format(tweet_length, max_tweet_length - tweet_length)


#phone = "315-555-2955"
#print "My phone number is ({0}) {1}.".format(phone[:3], phone[4:])
