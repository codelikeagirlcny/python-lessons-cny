def txt_to_str(textfile):
    """
        Takes a simple text file, returns one string of entire file contents.
    """

    with open(textfile, "r") as textfile_contents:
        text_string = textfile_contents.read()
    return text_string

statefile_contents = txt_to_str('states.txt')
#print statefile_contents

def delimfile_to_list(the_file, delim = ','):
#def delimfile_to_list2(the_file, delim1='\n', delim2 = ','):
    """
        Takes a delimited file, returns a list of lists (split by newline then by delimiter).
    """

    with open(the_file, "r") as filecontent:
         list_of_stuff_in_file = filecontent.read().split("\n")
    for index, item in enumerate(list_of_stuff_in_file):
        list_of_stuff_in_file[index] = item.split(delim)

    return list_of_stuff_in_file

state_delimfile_contents1 = delimfile_to_list('states.txt', '\t')
#state_delimfile_contents1 = delimfile_to_list2('states.txt', delim2 = '\t')
state_delimfile_contents2 = delimfile_to_list('states.csv')

print state_delimfile_contents1[0:5]
print state_delimfile_contents2[0:5]

