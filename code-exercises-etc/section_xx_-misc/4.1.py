def remove_duplicates(from_list):

    """
        The function list() will convert an item to a list.
        The function set() will convert an item to a set.

        A set is similar to a list, but all values must be unique.

        Converting a list to a set removes all duplicate values.
        We then convert it back to a list since we're most comfortable working with lists.

    """

    converted_from_list = list(set(from_list))

    return converted_from_list


my_list = ['AL,Alabama','AL,Alabama','AL,Alabama', 'AK,Alaska','AK,Alaska', 'AZ,Arizona', 'AR,Arkansas', 'CA,California', 'CA,California', 'CA,California', 'CO,Colorado', 'CT,Connecticut']
print "my_list before de-duping:"
print my_list
print '\n\n'

deduped_mylist = remove_duplicates(my_list)
print "my_list after de-duping:"
print deduped_mylist



def greeting(the_name):
    'Just some help text, to help you out.'
    the_greeting = 'Hello, {0}!'.format(the_name)
    return the_greeting

#your_name = raw_input('Enter your name: ').strip()
#your_name = your_name.strip()

#print greeting(your_name)

#print greeting(raw_input('Enter your name: ').strip())
