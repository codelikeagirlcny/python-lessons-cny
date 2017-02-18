#### loops! ####
# for each ITEM in this LIST...
# ...do something with that ITEM.

attendees = ['Alison', 'Belen', 'Rebecca', 'Nura']
# for each ITEM (person) in this LIST (attendees)...
for person in attendees:
    # ...do something with that ITEM (person).
    print person

    # first time thru:
    # person = "Alison"
    # print person -> "Alison"

    # second time thru:
    # person = "Belen"
    # print person -> "Belen"


ten_numbers = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for each ITEM (number) in this LIST (ten_numbers)...
for number in ten_numbers:
    # ...do something with that ITEM (number).
    print number

for number_z in range(10):
    print number_z

#### except... ####
# Sometimes you just need to do a thing a certain number of times -- i.e.
# for each ITEM in this LIST...
# ...do something -- but not with that ITEM, just do something over and over.

# make a list of 10 addresses
list_of_addresses = []
for number in range(10):
    # do this "something," 10 times.
    address = raw_input("Enter an address. ")
    list_of_addresses.append(address)
