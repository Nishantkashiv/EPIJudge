from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) == 0:
        return []
    elif len(square_matrix) == 1:
        return [square_matrix[0][0]]
    elif len(square_matrix) == 2:
        return [
            square_matrix[0][0], 
            square_matrix[0][1], 
            square_matrix[1][1], 
            square_matrix[1][0]
            ]
    r = []
    # Top row
    r.extend(square_matrix[0])

    # Last column
    for i in range(1, len(square_matrix)-1):
        r.append(square_matrix[i][-1])
    
    # Last row reverse
    r.extend(square_matrix[-1][::-1])

    # First column reverse
    for i in range(len(square_matrix)-2, 0, -1):
        r.append(square_matrix[i][0])
    if len(square_matrix) < 3:
        return r
    else:
        sub_matrix = [x[1:-1] for x in square_matrix[1:-1]]
        r.extend(matrix_in_spiral_order(sub_matrix))
    return r



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
