import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if l0 is None or l1 is None:
        return None
    pASwapped = False
    pBSwapped = False
    pA  = l0
    pB  = l1
    while not (pA is pB) and (pA is not None) and (pB is not None):
        pA = pA.next
        pB = pB.next
        if pA is None:
            if not pASwapped:
                pA = l1
                pASwapped = True
            else:
                return None
                
        if pB is None:
            if not pBSwapped:
                pB = l0
                pBSwapped = True
            else:
                return None
    if pA is not None and pB is not None:
        return pA
    else:
        return pB


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
