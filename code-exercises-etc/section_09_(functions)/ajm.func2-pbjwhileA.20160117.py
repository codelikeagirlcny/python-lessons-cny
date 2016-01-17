def pbjtime(bread_slices, pb, jelly):
    output = ""

    #set the number of sandwiches made (initialize sandwiches variable)
    sandwiches = 0

    while bread_slices >= 2 and pb >=1 and jelly >=1:
      # Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.
      sandwiches = sandwiches + 1
      output += "\nMaking sandwich #{0}".format(sandwiches)
      bread_slices = bread_slices - 2
      pb = pb - 1
      jelly = jelly - 1
      
      # How many sandwiches-worth of each ingredient remains?
      if min(bread_slices/2, pb, jelly) > 0:
        output += "\nI have enough bread for {0} more sandwich(es), enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread_slices/2,pb,jelly)
      elif bread_slices <= 1:
        output += "\nAll done; I ran out of bread."
      elif pb == 0:
        output += "\nAll done; I ran out of peanut butter."
      elif jelly == 0:
        output += "\nAll done; I ran out of jelly"
      else:
        output += "\nI am confused about remaining ingredient amounts."

    # If while conditional expression is False, we cannot make sandwiches.
    if sandwiches == 0:
      output += "\nThere aren't enough ingredients to make a sandwich."

    return output
    #return output, sandwiches

#pbjtime_output = pbjtime(10, 3, 0)
#print pbjtime_output

print pbjtime(10, 3, 6)

#output_text, num_sandwiches = pbjtime(10,3,6)
#print 'Here is what happened:{0}\n\nHow many sandwiches I made: {1}'.format(output_text, num_sandwiches)

# #get the ingredient amounts
# how_much_bread = raw_input("How many slices of bread do you have? ")
# pb = raw_input("How many servings of peanut butter do you have? ")
# jelly = raw_input("How many servings of jelly do you have? ")
# #convert the string input variables into integers
# how_much_bread = int(how_much_bread)
# pb = int(pb)
# jelly = int(jelly)
# print pbjtime(how_much_bread, pb, jelly)
