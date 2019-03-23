from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    import heapq
    idxs = [0 for _ in range(len(sorted_arrays))]
    res = []
    heap = []
    for idx in range(len(sorted_arrays)):
        heapq.heappush(heap, (sorted_arrays[idx][0], idx))
    while heap:
        val, list_idx = heapq.heappop(heap)
        res.append(val)
        idxs[list_idx] += 1
        if idxs[list_idx] < len(sorted_arrays[list_idx]):
            heapq.heappush(heap, (sorted_arrays[list_idx][idxs[list_idx]], list_idx))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
