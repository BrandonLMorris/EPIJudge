import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    # O(k) time, O(1) space solution
    if node0 is node1:
        return node0
    depth0, depth1 = 0, 0
    node = node0
    while node.parent is not None:
        node = node.parent
        depth0 += 1
    node = node1
    while node.parent is not None:
        node = node.parent
        depth1 += 1
    while depth0 != depth1:
        if depth0 > depth1:
            node0 = node0.parent
            depth0 -= 1
        else:
            node1 = node1.parent
            depth1 -= 1
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0


def o_k_solution(node0, node1):
    # O(k) solution, k is tree height
    ancestors = {node0}
    node = node0.parent
    while node is not None:
        ancestors.add(node)
        node = node.parent
    node = node1
    while node is not None and node not in ancestors:
        node = node.parent
    return node


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
