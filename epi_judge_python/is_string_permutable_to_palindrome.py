from test_framework import generic_test


def can_form_palindrome(s):
    # Convert string into counts of each character
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    # Check if every count (except at most one) is even
    found_odd = False
    for c, count in counts.items():
        if count % 2 != 0:
            if found_odd:
                return False
            else:
                found_odd = True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
