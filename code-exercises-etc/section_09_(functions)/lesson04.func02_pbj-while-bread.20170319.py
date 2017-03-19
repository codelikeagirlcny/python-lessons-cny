def make_sandwiches(bread_slices):
    """
        helpful information about the function...
    """

    #set the number of sandwiches made (initialize sandwiches variable)
    sandwiches = 0
    output = ''

    while bread_slices >= 2:
            sandwiches = sandwiches + 1
            output += 'I am making a sandwich #{0}!'.format(sandwiches)
            bread_slices = bread_slices - 2
            output += '\nI have enough bread for {0} more sandwiches.\n'.format(bread_slices / 2)
    return output, sandwiches

#get the ingredient amounts
bread_slices = raw_input('How many slices of bread do you have? ')

#convert the string input variables into integers
bread_slices = int(bread_slices)

msg, num_sandwiches = make_sandwiches(bread_slices)
print 'I can make ', num_sandwiches, 'sandwiches.'
#print msg

