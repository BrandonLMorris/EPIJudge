from test_framework import generic_test, test_utils


def permutations(A):

    def perms_inner(prefix, possible):
        if len(possible) == 0:
            return prefix
        return [(prefix + [possible[i]], possible[0:i] + possible[i+1:]) for i in range(len(possible))]
    possible = perms_inner([], A)
    for _ in range(len(A) - 1):
        tmp = []
        for t in possible:
            tmp.extend(perms_inner(*t))
        possible = tmp
    return [p[0] for p in possible]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
