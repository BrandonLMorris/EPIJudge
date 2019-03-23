from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    def count_letters(letter):
        letter_count = {}
        for c in letter:
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 0
        return letter_count
    letter_counts = count_letters(letter_text)
    mag_counts = count_letters(magazine_text)
    for k in letter_counts.keys():
        if k not in mag_counts:
            return False
        if letter_counts[k] > mag_counts[k]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
