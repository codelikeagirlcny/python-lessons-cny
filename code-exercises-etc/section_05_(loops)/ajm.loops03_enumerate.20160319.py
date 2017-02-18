
twitter_handles = ['@alisonjo2786', '@sarahroche', '@kseniahogan']

##for handle in twitter_handles:
##    print handle

for index, handle in enumerate(twitter_handles):
    ##print index
    ##print handle

    at_sign_index = handle.find('@')
    handle_without_at_sign = handle[at_sign_index + 1:]

    twitter_handles[index] = handle_without_at_sign

print twitter_handles

