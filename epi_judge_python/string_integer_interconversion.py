from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x < 0:
        is_neg = True
        x *= -1
    else:
        is_neg = False
    res = ''
    while x >= 10:
        res = (chr(ord('0') + (x % 10))) + res
        x = x // 10
    res = (chr(ord('0') + (x % 10))) + res
    return ('-' if is_neg else '') + res


def string_to_int(s):
    if s[0] == '-':
        is_neg = True
        s = s[1:]
    else:
        is_neg = False
    res = 0
    for idx, c in enumerate(s):
        res *= 10
        res += ord(c) - ord('0')
    return res * -1 if is_neg else res


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
