##with open("states.txt", "r") as states_file:
##    states = states_file.read()
##print states

with open("states.txt", "r") as states_file:
    states = states_file.read().split("\n")
    #states = states_file.read()
    #states = states.split("\n")

print states
print states[0]
print states[1]
print states[2]
