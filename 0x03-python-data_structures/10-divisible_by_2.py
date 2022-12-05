#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = my_list.copy()
    for i in range (len(result_list)):
        if result_list[i] % 2 == 0:
            result_list[i] = True
        else:
            result_list[i] = False
    return result_list       
