from test_framework import generic_test


def levenshtein_distance(A, B):
    dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    for idx in range(len(A)+1):
        dp[0][idx] = idx
    for idx in range(len(B)+1):
        dp[idx][0] = idx
    for row in range(1, len(B) + 1):
        for col in range(1, len(A) + 1):
            if A[col-1] == B[row-1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row][col] = 1 + min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])
    print(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
