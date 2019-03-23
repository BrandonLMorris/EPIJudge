from test_framework import generic_test


def search_first_of_k(A, k):
    # Binary search followed by binary search
    if not A:
        return -1
    left, right = 0, len(A) - 1
    mid = (left + right) // 2
    while A[mid] != k and left < right:
        if A[mid] <= k:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    if A[mid] != k:
        return -1
    assert A[mid] == k
    # Search the left half for smaller instances of k
    left, right = 0, mid
    mid = (left + right) // 2
    while left < right:
        if A[mid] == k:
            right = mid
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
