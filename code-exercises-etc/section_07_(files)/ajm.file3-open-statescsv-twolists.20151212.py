state_abbrs = []
state_names = []

with open('states.csv', 'r') as states_file:
    states = states_file.read().split('\n')

for index,state in enumerate(states):
    states[index] = state.split(',')
    
    state_abbrs.append(states[index][0])
    state_names.append(states[index][1])

print 'List of state abbreviations:\n{0}'.format(state_abbrs)
print 'List of state names:\n{0}'.format(state_names)

#print states[0][0]
