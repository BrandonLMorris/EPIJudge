from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # 13.6
    # Note: Could be optimized by only storing the min distance and last occurrence of each
    # word, rather than every occurrence
    word_idxs = {}
    for idx, word in enumerate(paragraph):
        if word not in word_idxs:
            word_idxs[word] = []
        word_idxs[word].append(idx)
    min_dist = float('inf')
    for word, indexes in word_idxs.items():
        for idx in range(len(indexes) - 1):
            dist = indexes[idx+1] - indexes[idx]
            if dist < min_dist:
                min_dist = dist
    return min_dist if min_dist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
