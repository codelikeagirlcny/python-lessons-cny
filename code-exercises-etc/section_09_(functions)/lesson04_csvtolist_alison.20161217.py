# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries, create a function that will open a CSV file and return the result as a nested list.

def csv_to_list(filename, delim = ","):
    """This function takes a CSV file and returns a list of data rows."""
    
    with open(filename, "r") as csv_file:
        data_rows = csv_file.read().split("\n")

    for index, row in enumerate(data_rows):        
        data_rows[index] = row.split(delim)

    return data_rows

list_of_survey_data = csv_to_list("..\survey.csv")
print list_of_survey_data
