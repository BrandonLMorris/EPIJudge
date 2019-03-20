import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head):
    # O(1) space solution
    if head is None:
        return None
    slow, fast = head, head
    fast = fast.next
    if fast is None:
        return None
    fast = fast.next
    while fast is not None and fast.data != slow.data:
        try:
            fast = fast.next.next
        except AttributeError:
            return None
        slow = slow.next
    if fast is None:
        return None
    cycle_length = get_cycle_length(fast)
    runner, slow = head, head
    for _ in range(cycle_length):
        runner = runner.next
    while runner is not slow:
        runner, slow = runner.next, slow.next
    return slow


def get_cycle_length(head):
    slow = head.next
    fast = head.next.next
    length = 1
    while fast is not slow:
        length += 1
        fast = fast.next.next
        slow = slow.next
    return length


def linear_space(head):
    # Simple solution with O(n) space
    visited = set()
    node = head
    idx = 0
    while node is not None:
        if node.data in visited:
            return node
        visited.add(node.data)
        node = node.next
        idx += 1
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
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
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
