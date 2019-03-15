from test_framework import generic_test


def merge_two_sorted_lists(l, n):
    if l is None: return n
    if n is None: return l
    if l.data < n.data:
        res_head = l
        l = l.next
    else:
        res_head = n
        n = n.next
    ptr = res_head
    while l is not None and n is not None:
        if l.data < n.data:
            ptr.next = l
            l = l.next
        else:
            ptr.next = n
            n = n.next
        ptr = ptr.next
    while l is not None:
        ptr.next = l
        l = l.next
        ptr = ptr.next
    while n is not None:
        ptr.next = n
        n = n.next
        ptr = ptr.next

    return res_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
