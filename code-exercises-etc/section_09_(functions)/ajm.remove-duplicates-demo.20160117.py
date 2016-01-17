def remove_duplicates(from_list):

    """ 
        The function list() will convert an item to a list. 
        The function set() will convert an item to a set.

        A set is similar to a list, but all values must be unique.

        Converting a list to a set removes all duplicate values.
        We then convert it back to a list since we're most comfortable working with lists.

    """

    uniqueified_list = list(set(from_list))

    return uniqueified_list

sm_platforms = ['GitHub', 'Twitter', 'Facebook', 'GitHub', 'Vine', 'MySpace', 'YouTube', 'Facebook']
print sm_platforms

sm_platforms_unique = remove_duplicates(sm_platforms)
print sm_platforms_unique
