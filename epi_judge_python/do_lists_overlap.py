import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    """
    Detect if l0 has a cycle
    `Slow and fast pointer
    Slow increment by 1
    Fast increment by 2
    if fast points to none no cycle
    if eventually fast points to slow then cycle`
    Detect if l1 has a cycle
    If cycle calculate size of cycle
    Then calculate the start of the cycle return

    If no cycle then in both calculate overlap using the
    Swap pointer method used in the previous problem
    `When one pointer reaches null assign it to the second list 
    and when both the pointers are pointing to the same node return it
    """
    if not(l0 and l1):
        return None
    l0_cyclic, cycle_node_l0 = detect_cycle(l0)
    l1_cyclic, cycle_node_l1 = detect_cycle(l1)
    cycle_start_l0 = cycle_start_l1 = None
    cycle_length_l0 = cycle_length_l1 = 0
  
    if l0_cyclic and l1_cyclic:
        cycle_length_l0 = get_cycle_length(cycle_node_l0)
        cycle_start_l0 = get_cycle_start(l0, cycle_length_l0)
        cycle_length_l1 = get_cycle_length(cycle_node_l1)
        cycle_start_l1 = get_cycle_start(l1, cycle_length_l1)
    # l0 and l1 cyclic
    
        if cycle_length_l0 != cycle_length_l1:
            return None
        return cycle_start_l0 if node_in_cycle(cycle_start_l0, cycle_length_l0, cycle_start_l1) else None
    elif l0_cyclic:
        return None
    elif l1_cyclic:
        return None
    else:
        # Both are not cyclic
        return do_non_cyclic_list_overlap(l0, l1)

def do_non_cyclic_list_overlap(l0: ListNode, l1:ListNode) -> ListNode:
    l0_swapped = l1_swapped = False
    l0_current = l0
    l1_current = l1
    if l0 is None or l1 is None:
        return None
    while l0_current is not l1_current:
        l0_current = l0_current.next
        l1_current = l1_current.next
        if l0_current is None:
            if l0_swapped:
                return None
            l0_current = l1
        if l1_current is None:
            if l1_swapped:
                return None
            l1_current = l0
    return l0

def node_in_cycle(cycle_node: ListNode, cycle_length: int, test: ListNode) -> bool:
    current = cycle_node
    while current.next is not cycle_node:
        if current is test:
            return True
        current = current.next
    return False

def get_cycle_start(head: ListNode, cycle_length: int) -> ListNode:
    current = head
    while current.next:
        x = current
        for _ in range(cycle_length):
            x = x.next
        if x is current:
            return current
        current = current.next
    return None

def get_cycle_length(head: ListNode) -> int:
    c = 2
    current = head
    while True:
        for _ in range(c):
            current = current.next
        if current is head:
            return c
        c += 1
    return 0

def detect_cycle(head: ListNode) -> (bool, ListNode):
    # Fast and slow pointer method
    slow = fast = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        if slow and slow.next:
            slow = slow.next
        if fast.next is slow:
            return (True, slow)
    return (False, None)

@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
