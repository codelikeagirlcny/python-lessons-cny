with open("states.txt", "r") as states_file:
    states = states_file.read().split("\n")

#print states
#for state in states:
#    print "This is a state: {0}.".format(state)

#desired outcome: "states" list of two-item lists of strings, stgh
#like [ ['Alabama', 'AL'], ['Alaska', 'AK'], ['Arizona', 'AZ'] ]

#for index, state in enumerate(states):
    #print 'The state at index {0} is called {1}.'.format(index,state)

    #state number 0 equals 'AL   Alabama'
    #states[index] = state.split('\t')
    #state number 0 equals ['AL','Alabama']

    #in other words...
    #first_state = states[0].split('\t')
    #print first_state

#print states

state_abbrs = [] #we want this to be sthg like ['AL','AK','AZ' ...]
state_names = [] #we want this to be sthg like ['Alabama','Alaska','Arizona' ...]

for index, state in enumerate(states):
    states[index] = state.split('\t')

    #states is looking like [['AL', 'Alabama'], ['AK', 'Alaska'], ['AZ', 'Arizona']]

    print states[index][0] #print out the first part of each "states" list item
    print states[index][1] #print out the second part of each "states" list item

    #then:
    state_names.append(states[index][1])

print state_names
