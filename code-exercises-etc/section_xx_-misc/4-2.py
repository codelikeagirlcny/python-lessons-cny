def pbj_while(slices):
    output = ''
    while (slices > 0):
        slices = slices - 2
        if slices >= 2:
            output += 'I am making a sandwich! I have bread for {0} more sandwiches.\n'.format(slices / 2)
        elif slices < 2:
            output += 'I am making a sandwich! But, this is my last sandwich.'
    return output

print pbj_while(int(raw_input('How many slices of bread do you have? ')))
