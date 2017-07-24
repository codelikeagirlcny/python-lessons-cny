contacts = {
    "Alison" : {
        'phone':'315-481-2904',
        'twitter':'@alisonjo2786',
        'email':'alisonjo2786@gmail.com'
        },
    "Belen" : {
        'phone':"315-555-9876",
        'twitter':'@belenbelen'
        },
    "Rebecca" : {
        'phone':"315-555-1234",
        'email':'rwhite23@gmail.com',
        'twitter':'@rebeccaontwitter'
        }
    }

for contact_key, info in contacts.items():
    print """\n{0}'s contact info is:""".format(contact_key) # Alison's contact info is:

    # For each dict item (contact)...
    # Output the "info" stuffs -- the dict VALUES, in a way that makes sense to humans.

    #####
    # you can think of it like this...
    #####
    #print """PHONE_KEY: PHONE_VALUE
    #         TWITTER_KEY: TWITTER_VALUE
    #         EMAIL_KEY: EMAIL_VALUE""".format()

    #####
    # or like this! more mind-bendy, less code :)
    #####
    for info_key, info_value in info.items():
        #print """INFO_ITEM_KEY: INFO_ITEM_VALUE""".format()
        print "\t{0}: {1}".format(info_key,info_value)


        

