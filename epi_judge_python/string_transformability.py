from test_framework import generic_test


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    # 19.7
    # Build a graph, edges between words of distance one
    graph = {}
    for source in D:
        graph[source] = []
        for dest in D:
            if source == dest:
                continue
            if word_dist(source, dest) == 1:
                graph[source].append(dest)
    visited = set()
    to_visit = [(s, 0)]
    while to_visit:
        current, level = to_visit.pop(0)
        visited.add(current)
        if current == t:
            return level
        for neighbor in graph[current]:
            if neighbor not in visited:
                to_visit.append((neighbor, level+1))
    return -1


def word_dist(w1, w2):
    return sum([1 if c1 != c2 else 0 for (c1, c2) in zip(w1, w2)])


def non_graph_solution(D, s, t):
    # Not explicitly a graph, but similar idea
    visited = set()
    to_visit = [(s, 0)]
    while to_visit:
        current, level = to_visit.pop(0)
        visited.add(current)
        if current == t:
            return level
        for neighbor in get_neighbors(D, current):
            if neighbor not in visited:
                to_visit.append((neighbor, level + 1))
    return -1


def get_neighbors(dictionary, w):
    res = []
    for idx in range(len(w)):
        letters = list(w)
        for code in range(26):
            letters[idx] = chr(code + ord('a'))
            word = ''.join(letters)
            if word in dictionary:
                res.append(word)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
