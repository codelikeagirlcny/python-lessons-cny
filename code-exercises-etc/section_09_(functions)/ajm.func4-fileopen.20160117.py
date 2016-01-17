def textfile_to_string(filename_with_path):

    with open(filename_with_path, "r") as the_file:
      the_text = the_file.read()

    return the_text

file_contents = textfile_to_string('lessons.txt')
print file_contents
