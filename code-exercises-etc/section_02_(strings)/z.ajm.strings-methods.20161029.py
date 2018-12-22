twitter = "@alisonjo2786"
#print twitter.replace("@", "#")

#twitter.replace("@", "#")
#print twitter

twitter = twitter.replace("@", "#")
print twitter

#last_name = "oppedibango"
#print last_name.find("a")
#print last_name.find("c")
#print last_name.find("z")
#print last_name.find("E")

name = "Alison Oppedibango"
name_sep = name.find(" ")
lname = name[name_sep+1:]
print lname
# or.....
##lname_start = name_sep + 1
##lname = name[lname_start:]
##print lname

lname = lname.lower()
number_of_os = lname.count("o")
print number_of_os
