with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")

    for index, state in enumerate(states):
        # index = 0, state = "AL,Alabama"
        # index = 1, state = "AK,Alaska"
        
        states[index] = state.split(",")
        #states[index] = states[index].split(",")

print states

##states = ['AL,Alabama', 'AK,Alaska', 'AZ,Arizona', 'AR,Arkansas']
##print states[0]
##states[0] = states[0].split(",")
##print states[0]

##states = [ ["AL", "Alabama"], ["AK", "Alaska"], ["AR", "Arkansas"] ]

print states[0]
print states[1]

