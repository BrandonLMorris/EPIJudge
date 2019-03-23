from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    res = []
    ai, bi = 0, 0
    while ai < len(A) and bi < len(B):
        if A[ai] == B[bi]:
            if len(res) == 0 or res[-1] != A[ai]:
                res.append(A[ai])
            ai += 1
            bi += 1
        elif A[ai] < B[bi]:
            ai += 1
        else:
            bi += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
