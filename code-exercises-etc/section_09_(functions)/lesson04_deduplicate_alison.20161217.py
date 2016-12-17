# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/codelikeagirlcny/python-lessons-cny/blob/master/code-exercises-etc/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/codelikeagirlcny/python-lessons-cny/blob/master/code-exercises-etc/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

# copied from github (code-exercises-etc/section_09_(functions)/remove_duplicates.py)
def remove_duplicates(from_list):
    """
        The function list() will convert an item to a list.
        The function set() will convert an item to a set.

        A set is similar to a list, but all values must be unique.

        Converting a list to a set removes all duplicate values.
        We then convert it back to a list since we're most comfortable working with lists.

    """
    from_list = list(set(from_list))
    return from_list

# based on lesson 4 in-class exercise
def textfile_to_list(filename):
    """This function takes a file and returns a string of the file contents."""
    
    with open(filename, "r") as text_file:
        data_rows = text_file.read().split("\n")

    return data_rows

# Goal 1
film_attendees_list = textfile_to_list("../film_screening_attendees.txt")
#print film_attendees_list
hh_attendees_list = textfile_to_list("../happy_hour_attendees.txt")
#print hh_attendees_list

print len(film_attendees_list)
master_attendees_list = film_attendees_list
print len(film_attendees_list)
master_attendees_list.extend(hh_attendees_list)
####***************##############************########
print len(film_attendees_list)
print "\n\n"
print "\n\n"
#print master_attendees_list
print len(master_attendees_list)
master_attendees_list = remove_duplicates(master_attendees_list)
print master_attendees_list
print len(master_attendees_list)

print "\n\n"

# Goal 2

def find_in_both(list1, list2):
    """Takes two lists, returns items that are in both."""

    in_both = []
    for item in list1:
        if item in list2:
            in_both.append(item)
    return in_both

attendees_of_both = find_in_both(film_attendees_list, hh_attendees_list)
print attendees_of_both
print len(attendees_of_both)


