#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = {}
    new_set = set(new_set)
    for e in set_1:
        if not set_2.__contains__(e):
            new_set.add(e)
    for e in set_2:
        if not set_1.__contains__(e):
            new_set.add(e)
    return new_set
