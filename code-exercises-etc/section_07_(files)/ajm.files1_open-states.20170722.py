with open("states.txt", "r") as states_file:
    states = states_file.read()
#print states

with open("states.txt", "r") as states_file:
    #states = states_file.read()
    #states = states.split("\n")
    states = states_file.read().split("\n")
#print states

with open("states.csv", "r") as states_file:
    states_list = states_file.read().split("\n")
print states_list
#states_list = states_list.split(",")  # Error b/c states is a list!

for index, stname in enumerate(states_list):
    # First time thru, index is 0, stname is "AL,Alabama" --
    #   Change the 0th item in states_list to "AL,Alabama".split(",") --
    #   states_list[0] will be ["AL", "Alabama"]
    #
    # Second time thru, index is 1, stname is "AK,Alaska" --
    #   Change the 1th item in states_list to "AK,Alaska".split(",") --
    #   states_list[1] will be ["AK","Alaska"]
    states_list[index] = stname.split(',')
    #   or...    states_list[index] = states_list[index].split(',')
print "After splitting each list item..."
print states_list







