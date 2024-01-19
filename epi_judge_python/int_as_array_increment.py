from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    """
    [0] Just increment and return
    [1,1] Just increment and return
    [1,9] Increment and then carry to digit at higher unit
    [9,9] Increment and carry and increase length of array
    """
    carry = 1
    for i in range(len(A)-1, -1, -1):

        if A[i] + carry  < 10:
            A[i] = A[i] + carry
            carry = 0
            break
        else:
            A[i] = 0
            carry = 1
    if carry == 1:
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
