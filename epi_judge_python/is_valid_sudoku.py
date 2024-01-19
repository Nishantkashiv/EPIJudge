from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def all_uniques(A: List[int]):
        existing = {}
        for x in A:
            if x == 0:
                continue
            if x in existing:
                return False
            else:
                existing[x] = True
        return True
    def unique_box(A: List[List[int]]) -> bool:
        existing = {}
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    continue
                if A[i][j] in existing:
                    return False
                else:
                    existing[A[i][j]] = True
        return True
    print() 
    for i in range(len(partial_assignment)):
        if not all_uniques(partial_assignment[i]):
            return False
        # create column list
        col = [partial_assignment[j][i] for j in range(len(partial_assignment))]
        print(col)
        if not all_uniques(col):
            return False
    

    return True


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('is_valid_sudoku.py',
    #                                    'is_valid_sudoku.tsv', is_valid_sudoku))
    A = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 6, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 8, 0, 0, 0, 0], 
        [9, 0, 0, 0, 7, 5, 0, 0, 0], 
        [0, 0, 0, 0, 5, 0, 0, 8, 0], 
        [0, 0, 9, 0, 0, 0, 0, 0, 0], 
        [2, 0, 6, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    print(f"A: {A} \n is valid: {is_valid_sudoku(A)}")