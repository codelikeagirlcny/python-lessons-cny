state_abbrs = ''
state_names = ''

with open('states.csv', 'r') as states_file:
    states = states_file.read().split('\n')

for index,state in enumerate(states):
    states[index] = state.split(',')

    state_abbrs += states[index][0] + '\n'
    state_names += states[index][1] + '\n'

with open('ajm.state_abbreviations.20151212.txt', 'w') as abbr_file:
    abbr_file.write(state_abbrs)

with open('ajm.state_names.20151212.txt', 'w') as name_file:
    name_file.write(state_names)

#if we do this with lists of abbrs and names instead of
#strings (like in the previous exercise), we can convert
#the lists into strings:
#   state_abbrs_as_string = '\n'.join(state_abbrs)
#(and then write to the file)
