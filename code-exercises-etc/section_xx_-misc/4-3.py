def textfile_to_string(filename):
    'Returns contents of text file as string.'
    with open(filename, 'r') as text_file:
        text = text_file.read()
    return text

#print textfile_to_string('./repo/section_07_(files)/states.txt')

#def open_delimed_file(filename,delimiter=','):
    #your code goes here
