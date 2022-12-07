#!/usr/bin/python3
def uniq_add(my_list=[]):
	used_number = []
	sum = 0
	for i in range(len(my_list)):
		if not used_number.__contains__(my_list[i]):
			sum += my_list[i]
			used_number.append(my_list[i])
	return sum
