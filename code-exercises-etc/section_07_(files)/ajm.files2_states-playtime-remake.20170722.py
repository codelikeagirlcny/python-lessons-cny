with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")
#print states

for index, state in enumerate(states):
    states[index] = state.split(',')
    #I could fill out the abbrs/names lists while I'm up here, i.e.
    #   state_abbrs.append(states[index][0])

#print "\nAfter splitting each list item..."
#print states

state_abbrs = []
state_names = []

for state in states:
    # First time thru, state is ["AL","Alabama"]
    # Do state_abbrs.append("AL")
    state_abbrs.append(state[0])
    state_names.append(state[1])

#print "\nAfter filling in the abbrs/names lists..."
#print state_abbrs
#print state_names

output = "<select>\n"

for stname, stabbr in zip(state_names, state_abbrs):
    # <option value="AL">Alabama</option>
    output += '\t<option value="' + stabbr + '" >'  + stname + '</option>\n'

output += "</select>"
#print output

with open("states.html", "w") as new_file:
    new_file.write(output)
    # turns out, you can't do this in "w" mode!
    # html_output = new_file.read()

#print html_output














