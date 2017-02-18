## raw input basics!
## see also: https://github.com/codelikeagirlcny/python-lessons-cny/blob/master/code-exercises-etc/_raw_input.py
# name = raw_input("what is your name? ")
# print name

# User, tell me one DC address.
# I save that address as "address_1"
# I evaluate address_1 and add it to the appropriate "list_of_QUAD_addresses" list.
# Then we go through that process two more times, so that I've collected 3 addresses,
# and siphoned each into the correct QUAD list of addresses.

list_of_nw_addresses = []
list_of_ne_addresses = []
list_of_se_addresses = []
list_of_sw_addresses = []

## Soooo let's create address_1
## address_1 = "654 E Street SE Washington DC 20003"

address_1 = raw_input("Enter the first address. ")
address_2 = raw_input("Enter the second address. ")
address_3 = raw_input("Enter the third address. ")
print address_1
print address_2
print address_3


#### evaluate address 1! ####

#address_1_as_list = address_1.lower().split(" ")
#if "se" in address_1_as_list:
#    # add address 1 to the SE list

if " nw " in address_1.lower():
    # ok so, this address contains "NW"...
    # add address 1 to the NW list
    list_of_nw_addresses.append(address_1)
elif " ne " in address_1.lower():
    # add address 1 to the NE list
    list_of_ne_addresses.append(address_1)
elif " se " in address_1.lower():
    # add address 1 to the SE list
    list_of_se_addresses.append(address_1)
elif " sw " in address_1.lower():
    # add address 1 to the SW list
    list_of_sw_addresses.append(address_1)
else:
    print "Address 1 did not have any quadrant info."


#### evaluate address 2! ####

if " nw " in address_2.lower():
    list_of_nw_addresses.append(address_2)
elif " ne " in address_2.lower():
    list_of_ne_addresses.append(address_2)
elif " se " in address_2.lower():
    list_of_se_addresses.append(address_2)
elif " sw " in address_2.lower():
    list_of_sw_addresses.append(address_2)
else:
    print "Address 2 did not have any quadrant info."


#### evaluate address 3! ####

if " nw " in address_3.lower():
    list_of_nw_addresses.append(address_3)
elif " ne " in address_3.lower():
    list_of_ne_addresses.append(address_3)
elif " se " in address_3.lower():
    list_of_se_addresses.append(address_3)
elif " sw " in address_3.lower():
    list_of_sw_addresses.append(address_3)
else:
    print "Address 3 did not have any quadrant info."

print "\n"

print "{0} NW addresses: {1}".format(len(list_of_nw_addresses), list_of_nw_addresses)
print "{0} NE addresses: {1}".format(len(list_of_ne_addresses), list_of_ne_addresses)
print "{0} SE addresses: {1}".format(len(list_of_se_addresses), list_of_se_addresses)
print "{0} SW addresses: {1}".format(len(list_of_sw_addresses), list_of_sw_addresses)
