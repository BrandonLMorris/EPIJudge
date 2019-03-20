from test_framework import generic_test


def square_root(k):
    left, right = 0, k
    mid = (left + right) // 2
    while left < right:
        if mid * mid > k:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    # Check for off by one
    if mid * mid > k:
        mid -= 1
    return mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
