from collections import Counter

SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def check_lists(l1, l2):
    if l1 == l2:
        return EQUAL
    elif is_sublist(l1, l2):
        return SUBLIST
    elif is_sublist(l2, l1):
        return SUPERLIST
    else:
        return UNEQUAL

def is_sublist(sublist, container):
    if len(sublist) == 0:
        return True
    firsts = [i for i, j in enumerate(container) if j == sublist[0]]
    if firsts:
        for i in firsts:
            if sublist == container[i:i+len(sublist)]:
                return True
    return False
