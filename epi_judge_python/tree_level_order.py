from test_framework import generic_test


def binary_tree_depth_order(tree):
    return queue_solution(tree)


def queue_solution(tree):
    if tree is None:
        return []
    res = []
    nodes_to_consider = [tree]
    while len(nodes_to_consider) > 0:
        res.append([n.data for n in nodes_to_consider])
        new_nodes_to_consider = []
        for node in nodes_to_consider:
            if node.left is not None:
                new_nodes_to_consider.append(node.left)
            if node.right is not None:
                new_nodes_to_consider.append(node.right)
        nodes_to_consider = new_nodes_to_consider
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
