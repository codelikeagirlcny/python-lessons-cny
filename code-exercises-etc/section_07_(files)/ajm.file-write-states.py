with open("states.txt", "r") as states_file:
    states = states_file.read().split("\n")

state_abbrs = [] #we want this to be sthg like ['AL','AK','AZ' ...]
state_names = [] #we want this to be sthg like ['Alabama','Alaska','Arizona' ...]

for index, state in enumerate(states):
    states[index] = state.split('\t')

    state_names.append(states[index][1])
    state_abbrs.append(states[index][0])

#print state_names
#print state_abbrs

abbreviations_string = ''
#abbreviations_string = str(state_abbrs)
names_string = ''

for abbr in state_abbrs:
    abbreviations_string += abbr
    abbreviations_string += '\n'
abbreviations_string = abbreviations_string.strip()
#print abbreviations_string

for name in state_names:
    names_string += name
    names_string += '\n'
names_string = names_string.strip()
#print names_string

with open('state_abbrs.txt', 'w') as abbrs_file:
    abbrs_file.write(abbreviations_string)

with open('state_names.txt', 'w') as names_file:
    names_file.write(names_string)
