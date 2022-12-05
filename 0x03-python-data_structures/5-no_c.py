#!/usr/bin/env python3
def no_c(my_string):
    for c in my_string:
        if c == 'c' or c == 'C':
            c = ''
    return my_string
