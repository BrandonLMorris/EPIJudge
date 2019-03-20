import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # Remove b's and replace a's with dd
    res_idx = len(s) - 1
    in_idx = size - 1
    while in_idx >= 0:
        if s[in_idx] == 'b':
            in_idx -= 1
        elif s[in_idx] == 'a':
            s[res_idx] = 'd'
            res_idx -= 1
            s[res_idx] = 'd'
            res_idx -= 1
            in_idx -= 1
        else:
            s[res_idx] = s[in_idx]
            res_idx -= 1
            in_idx -= 1
    for toi, fromi in enumerate(range(res_idx + 1, len(s))):
        s[toi] = s[fromi]
    return len(s) - res_idx - 1


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
