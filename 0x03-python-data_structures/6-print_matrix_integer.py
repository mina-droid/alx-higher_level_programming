#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(col), end=" " if j != i[-1] else "")
        print()
