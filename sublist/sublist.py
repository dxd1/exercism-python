SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def check_lists(l1, l2):
    if l1 == l2:
        return EQUAL
