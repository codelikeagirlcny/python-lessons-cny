#create lists for each quadrant of addresses
NWaddresses = []
NEaddresses = []
SEaddresses = []
SWaddresses = []

for number in range(3):
    address = raw_input('Enter an address. ')
    if ' nw ' in address.lower():
        NWaddresses.append(address)
    elif ' ne ' in address.lower():
        NEaddresses.append(address)
    elif ' se ' in address.lower():
        SEaddresses.append(address)
    elif ' sw ' in address.lower():
        SWaddresses.append(address)
    else:
        print 'Could not match address with a quadrant.'
        #exit()


print "\n There are {0} addresses in the NW quadrant: {1}.".format(len(NWaddresses), NWaddresses)
print "There are {0} addresses in the NE quadrant: {1}.".format(len(NEaddresses), NEaddresses)
print "There are {0} addresses in the SE quadrant: {1}.".format(len(SEaddresses), SEaddresses)
print "There are {0} addresses in the SW quadrant: {1}.".format(len(SWaddresses), SWaddresses)

