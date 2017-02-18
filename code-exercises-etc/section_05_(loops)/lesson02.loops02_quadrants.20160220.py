nw_quadrant = []
ne_quadrant = []
se_quadrant = []
sw_quadrant = []

for number in range(3):
    address = raw_input('Enter an address. ')
    if 'nw' in address.lower():
        nw_quadrant.append(address)
    elif 'ne' in address.lower():
        ne_quadrant.append(address)
    elif 'se' in address.lower():
        se_quadrant.append(address)
    elif 'sw' in address.lower():
        sw_quadrant.append(address)
    else:
        print 'Could not place address #{0} into a quadrant list.'.format(number + 1)

print "\nNumber of addresses in NW quadrant: {0}".format(len(nw_quadrant))
print "Addresses in NW quadrant: {0}".format(nw_quadrant)

print "\nNumber of addresses in NE quadrant: {0}".format(len(ne_quadrant))
print "Addresses in NE quadrant: {0}".format(ne_quadrant)

print "\nNumber of addresses in SE quadrant: {0}".format(len(se_quadrant))
print "Addresses in SE quadrant: {0}".format(se_quadrant)

print "\nNumber of addresses in SW quadrant: {0}".format(len(sw_quadrant))
print "Addresses in SW quadrant: {0}".format(sw_quadrant)
