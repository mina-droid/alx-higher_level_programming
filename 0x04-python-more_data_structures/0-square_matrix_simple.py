#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    for r in range(len(new_matrix)):
        for c in range(len(new_matrix[r])):
            new_matrix[r][c] = pow(new_matrix[r][c], 2)
    return new_matrix
