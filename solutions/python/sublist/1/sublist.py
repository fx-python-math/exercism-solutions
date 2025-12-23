"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == [] and list_two != []:
        return SUBLIST
    if list_two == [] and list_one != []:
        return SUPERLIST
    
    
    matchings_one = [list_one[i:i+len(list_two)] for i in range(max(0, len(list_one) - len(list_two) + 1))]
    matchings_two = [list_two[i:i+len(list_one)] for i in range(max(0, len(list_two) - len(list_one) + 1))]

    

    if list_one in matchings_two and list_one != list_two:
        return SUBLIST
    elif list_two in matchings_one and list_one != list_two:
        return SUPERLIST
    elif list_one == list_two:
        return EQUAL
    else:
        return UNEQUAL
    
    
    

