from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    """"O(n) space variant, still O(n*s) time where s is number of play scores"""
    counts = [0 for _ in range(final_score+1)]
    # Can always score zero points
    counts[0] = 1
    for score in individual_play_scores:
        for idx in range(final_score+1):
            if idx - score >= 0:
                counts[idx] += counts[idx - score]
    return counts[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
