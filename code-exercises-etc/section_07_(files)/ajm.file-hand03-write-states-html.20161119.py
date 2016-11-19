with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")

    for index, state in enumerate(states):
        states[index] = state.split(",")
        #state_abbrs.append(states[index][0])

#print states

# Step 1: put all the abbrs in a list of abbrs,
# and put all names in a list of names!
state_abbrs = []
state_names = []

for state in states:
    #state = ["AL","Alabama"]
    #state = ["AK","Alaska"]
    state_abbrs.append(state[0])
    state_names.append(state[1])
#print state_abbrs
#print state_names

# Step 2: Loop through each list and put the values
# into the add HTML...
##print '<select name="state">'
##print '\t<option value="">Select a state</option>'
##
##for abbr, name in zip(state_abbrs, state_names):
##    print '\t<option value="{0}">{1}</option>'.format(abbr,name)
##
##print '</select>'

# Step 3: now get fancy and put that <select>
# into an HTML file...
states_option_list = ""
states_option_list += '<select name="state">'
#print states_option_list
states_option_list += '\t<option value="">Select a state</option>'

for abbr, name in zip(state_abbrs, state_names):
    states_option_list += '\t<option value="{0}">{1}</option>'.format(abbr,name)

states_option_list += '</select>'

with open("states.html", "w") as new_file:
    new_file.write(states_option_list)

##states_option_list2 = """
##<select name="state">
##\t<option value="">Select a state</option>
##"""
