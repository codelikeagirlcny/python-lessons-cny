twitter = "@alisonjo2786"
print twitter[0]

address = "123 Some Street Somewhere NY 13555"
print address

print address[-5:]

phone = "315-555-5555"
print "Call {0} for great pizza".format(phone[4:])

greeting = "Hello {0}"
print greeting.format("Alison")

print "Area code: {0}".format("131")

email = "alisonexample@gmail.com"
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



email_alison = "alisonexample@gmail.com"
email_tim = "timothyexample@gmail.com"

email_length_alison = len(email_alison)
print email_length_alison
email_length_tim = len(email_tim)
print email_length_tim

if email_length_alison < email_length_tim:
    print "alison's email is shorter"


email_bad = "alison@example@gmail.com"
print email_bad.count("@")
