
twitter_handles = ['@alisonjo2786', '@sarahroche', '@kseniahogan']

##for handle in twitter_handles:
##    print handle

for index, handle in enumerate(twitter_handles):
    ##print index
    ##print handle

    at_sign_index = handle.find('@')
    handle_without_at_sign = handle[at_sign_index + 1:]

    twitter_handles[index] = handle_without_at_sign

print twitter_handles


#### ALSO ####
# This example was "stolen" from ajm.lists01_attendees.20160220.py

attendees = ['Shannon', 'Jenn', 'Grace']
for index, attendee in enumerate(attendees):
    attendees[index] = 'Ms. ' + attendee

print attendees
print attendee

##for attendee in attendees:
##    attendee = 'Ms. ' + attendee
