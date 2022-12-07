#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_integer = 0
    if len(roman_string) == 1:
        return roman_dict[roman_string]
    for i in range(len(roman_string)):
        if roman_dict.keys().__contains__(roman_string[i]):
            if i != len(roman_string) - 1:
                if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                    roman_integer += -roman_dict[roman_string[i]]
                else:
                    roman_integer += roman_dict[roman_string[i]]
            else:
                roman_integer += roman_dict[roman_string[i]]
    return roman_integer
