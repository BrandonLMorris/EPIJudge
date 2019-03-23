from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:
    # 13.3
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.use_counter = 0
        return

    def lookup(self, isbn):
        if isbn in self.cache:
            price, _ = self.cache[isbn]
            self.cache[isbn] = (price, self.use_counter)
            self.use_counter += 1
            return self.cache[isbn][0]
        return -1

    def insert(self, isbn, price):
        # O(c) solution, where c is capacity
        #   Alternative: Keep a min heap of the cache sorted by its use_counter value. Evicting involves just popping
        #   the isbn at the top of the heap
        # Don't update price if in cache already
        if isbn in self.cache.keys():
            old_price, _ = self.cache[isbn]
            self.cache[isbn] = (old_price, self.use_counter)
            self.use_counter += 1
        else:
            # Evict if over capacity
            if len(self.cache) == self.capacity:
                least_recent, least_counter = None, None
                for isbn_, (_, counter) in self.cache.items():
                    if least_recent is None or counter < least_counter:
                        least_counter = counter
                        least_recent = isbn_
                self.cache.pop(least_recent)
                self.cache[isbn] = (price, self.use_counter)
            else:
                self.cache[isbn] = price, self.use_counter
            self.use_counter += 1
        return

    def erase(self, isbn):
        if isbn in self.cache:
            self.cache.pop(isbn)
            return True
        return False


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
