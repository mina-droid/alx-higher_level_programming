#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score_key = list(a_dictionary.items())[0][0]
    max_score_value = list(a_dictionary.items())[0][1]
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_score_value:
            max_score_key = key
            max_score_value = a_dictionary[key]
    return max_score_key
