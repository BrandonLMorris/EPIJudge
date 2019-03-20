from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    if num_as_string[0] == '-':
        is_neg = True
        num_as_string = num_as_string[1:]
    else:
        is_neg = False
    base10 = 0
    for exp, val in enumerate(reversed(num_as_string)):
        base10 += hex_to_int(val) * (b1 ** exp)
    assert base10 >= 0
    res = ''
    div, mod = divmod(base10, b2)
    while div > 0:
        res = int_to_hex(mod) + res
        div, mod = divmod(div, b2)
    res = int_to_hex(mod) + res
    return ('-' if is_neg else '') + res


def int_to_hex(x):
    if x < 10:
        return str(x)
    return chr(ord('A') + (x - 10))


def hex_to_int(h):
    if ord(h) - ord('A') < 0:
        return ord(h) - ord('0')
    return 10 + ord(h) - ord('A')



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
