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

#print contacts
#print contacts.keys()
#print contacts.values()

##for contact_KEY in contacts.keys():
##    print contact_KEY
##
##for contact_k, contact_v in zip(contacts.keys(),contacts.values()):
##    print contact_k, " -- ", contact_v, "\n"

for contact in sorted(contacts.keys()):
    #print contact # "Alison"
    #print contacts[contact]['email']
    #No! Use .get() b/c it's better, and our program won't throw an error when it gets to Belen...
    print contacts.get(contact).get('email')

for contact_key, info in contacts.items():
    print contact_key, ' ', info














