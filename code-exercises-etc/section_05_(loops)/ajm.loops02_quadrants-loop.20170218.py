list_of_nw_addresses = []
list_of_ne_addresses = []
list_of_se_addresses = []
list_of_sw_addresses = []

for number in range(3):
    address = raw_input("Enter an address. ")

    if " nw " in address.lower():
        list_of_nw_addresses.append(address)
    elif " ne " in address.lower():
        list_of_ne_addresses.append(address)
    elif " se " in address.lower():
        list_of_se_addresses.append(address)
    elif " sw " in address.lower():
        list_of_sw_addresses.append(address)
    else:
        print "Address {0} did not have any quadrant info.".format(number)

print "\n"

print "{0} NW addresses: {1}".format(len(list_of_nw_addresses), list_of_nw_addresses)
print "{0} NE addresses: {1}".format(len(list_of_ne_addresses), list_of_ne_addresses)
print "{0} SE addresses: {1}".format(len(list_of_se_addresses), list_of_se_addresses)
print "{0} SW addresses: {1}".format(len(list_of_sw_addresses), list_of_sw_addresses)
