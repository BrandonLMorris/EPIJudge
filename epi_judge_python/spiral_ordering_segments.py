from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    res = []
    n = len(square_matrix)
    row, col = 0, 0
    while n > 0:
        if n == 1:
            res.append(square_matrix[row][col])
            break
        for _ in range(n-1): # Moving right
            res.append(square_matrix[row][col])
            col += 1
        for _ in range(n-1): # Moving down
            res.append(square_matrix[row][col])
            row += 1
        for _ in range(n-1): # Moving left
            res.append(square_matrix[row][col])
            col -= 1
        for _ in range(n-2): # Moving up
            res.append(square_matrix[row][col])
            row -= 1
        res.append(square_matrix[row][col])
        # Move right one spot
        col += 1
        n -= 2
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
