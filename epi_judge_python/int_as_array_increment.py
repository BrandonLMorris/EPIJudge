from test_framework import generic_test


def plus_one(A):
    # 6.2
    idx = len(A) - 1
    carry = 1
    while idx >= 0 and carry:
        A[idx] += carry
        carry, res = divmod(A[idx], 10)
        A[idx] = res
        idx -= 1
    if carry:
        A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
