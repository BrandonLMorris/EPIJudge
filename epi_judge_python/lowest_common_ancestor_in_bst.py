import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    # 15.4
    node = tree
    while node is not None:
        if node.data == s.data or node.data == b.data:
            break
        if s.data < node.data < b.data:
            break
        if node.data < s.data:
            node = node.right
        else:
            node = node.left
    return node


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_LCA, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_in_bst.py",
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
