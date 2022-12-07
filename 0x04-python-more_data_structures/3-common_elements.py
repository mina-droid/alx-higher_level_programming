#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = {}
    new_set = set(new_set)
    for e in set_1:
        if set_2.__contains__(e):
            new_set.add(e)
    return new_set
