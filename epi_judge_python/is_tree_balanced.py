from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def is_balanced_inner(node):
        if node is None:
            return 0
        left = is_balanced_inner(node.left)
        right = is_balanced_inner(node.right)
        if left is False or right is False or abs(left - right) > 1:
            return False
        return max(left, right) + 1
    balanced = is_balanced_inner(tree)
    return not (balanced is False)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
