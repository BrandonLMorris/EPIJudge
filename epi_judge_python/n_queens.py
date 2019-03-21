from test_framework import generic_test


def n_queens(n):
    boards = []

    def queens_inner(row, queens):
        if row == n:
            boards.append(queens.copy())
        else:
            for col in range(n):
                queens.append(col)
                if is_valid(queens):
                    queens_inner(row + 1, queens)
                queens.pop(-1)

    queens_inner(0, [])
    return boards




def is_valid(queens):
    positions = [(row, col) for row, col in enumerate(queens)]
    for i in range(len(queens) - 1):
        for j in range(i + 1, len(queens)):
            q1, q2 = positions[i], positions[j]
            if (q1[0] == q2[0] or q1[1] == q2[1] or
                    abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])):
                return False
    return True


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
