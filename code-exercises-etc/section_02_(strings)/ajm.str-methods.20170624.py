email = 'alisonjo2786@gmail.com'
print email.find("@")
print email.find("Z")
print email.find("A")


print "\n\n"

twitter = '@alisonjo2786'
#print twitter

print twitter.replace('@', '#')
print twitter

twitter = twitter.replace('@', '#')
print twitter

print "\n\n"

at_sign_position = email.find("@")
email_domain = email[at_sign_position+1:]
print at_sign_position
print email_domain

