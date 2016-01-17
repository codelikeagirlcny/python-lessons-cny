##with open('states.txt', 'r') as states_file:
##    states = states_file.read().split('\n')
##
##print states
##print '\n\n'
##
##for index,state in enumerate(states):
##    states[index] = state.split('\t')
##
##print states

with open('states.csv', 'r') as states_file:
    states = states_file.read().split('\n')

print states
print '\n\n'

for index,state in enumerate(states):
    states[index] = state.split(',')

print states
