from test_framework import generic_test


def number_of_ways(n, m):
    # m is the row
    mat = [[0 for _ in range(n)] for _ in range(m)]
    for col in range(n):
        mat[0][col] = 1
    for row in range(m):
        mat[row][0] = 1
    for row in range(1, m):
        for col in range(1, n):
            mat[row][col] = mat[row-1][col] + mat[row][col-1]
    return mat[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
