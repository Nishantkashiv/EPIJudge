import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    """
    Two iterators slow and fast.
    Slow will move one step at a time. 
    Fast will move 2 steps at a time.
    If Fast reaches null return false
    If slow and fast are at the same node return true
    """
    fast = slow = head
    cycle_length = 0
    while fast and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            """
            This means that the list contains a cycle
            Now calculate the lenght of the cycle
            """
            cycle_length = calculate_cycle_length(slow)
            return calculate_start_node(head, cycle_length)
    return None


def calculate_start_node(head: ListNode, cycle_length: int) -> ListNode: 
    it = head
    while True:
        it_plus_cycle = it
        for _ in range(cycle_length):
            it_plus_cycle = it_plus_cycle.next
        if it_plus_cycle is it:
            return it
        it = it.next
    return


def calculate_cycle_length(head: ListNode) -> int:
    """
    Keep a while loop with increasing cycle length
    when node + c hops == current node that is the cycle length
    """
    c = 2
    while True:
        current = head
        for _ in range(c):
            current = current.next
        if current is head:
            return c
        c += 1
    return

@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
