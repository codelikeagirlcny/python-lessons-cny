twitter = "@alisonjo2786"
print twitter[0]

address = "113 Park Street Groton NY 13073"
print address

print address[-5:]

phone = "315-481-2904"
print "Call {0} for great pizza".format(phone[4:])

greeting = "Hello {0}"
print greeting.format("Alison")

print "Area code: {0}".format("131")

email = "alisonjo2786@gmail.com"
print email
print email.find("@")
#at_sign = email.find("@")
#print at_sign
#print email[at_sign+1:]

#print email.find(2)

print email.find("z") # -1
print email.find('a')
print email.find('A')

twitter = "@cornell"
print twitter
print twitter.replace("@", "#")
print twitter

twitter = twitter.replace("@", "#")
print twitter

gender = "Female"
gender = gender.lower()
print gender



email_alison = "alisonjo2786@gmail.com"
email_tim = "tim.oppedisano@gmail.com"

email_length_alison = len(email_alison)
print email_length_alison
email_length_tim = len(email_tim)
print email_length_tim

if email_length_alison < email_length_tim:
    print "alison's email is shorter"


email_bad = "alison@jo@gmail.com"
print email_bad.count("@")
