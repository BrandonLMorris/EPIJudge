from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if tree is None:
        return True
    if tree.left is not None:
        if tree.left.data > tree.data or tree.left.data < low_range:
            return False
        left_is_bst = is_binary_tree_bst(tree.left, low_range, tree.data)
    else:
        left_is_bst = True
    if tree.right is not None:
        if tree.right.data < tree.data or tree.right.data > high_range:
            return False
        right_is_bst = is_binary_tree_bst(tree.right, tree.data, high_range)
    else:
        right_is_bst = True
    return left_is_bst and right_is_bst


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
