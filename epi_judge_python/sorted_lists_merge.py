from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1:
        return L2
    elif not L2:
        return L1
    result = None
    if L1.data <= L2.data:
        result = L1
        L1 = L1.next
    else:
        result = L2
        L2 = L2.next
    result_current = result
    while L1 or L2:
        if L1 and L2:
            if L1.data <= L2.data:
                result_current.next = L1
                L1 = L1.next
            else:
                result_current.next = L2
                L2 = L2.next
            result_current = result_current.next
        elif L1:
            result_current.next = L1
            return result
        elif L2:
            result_current.next = L2
            return result
    return result

    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
