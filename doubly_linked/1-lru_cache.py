#!/usr/bin/env python

# In this optimized implementation, we use the Ordered Dict
# API so we don't have to manually use a linked list to keep# items in order
# Ordered dict is implemented in Cpython so it's highly
# optimized

from collections import OrderedDict

class LRUCache:
    def __init__(self, size: int):
        self.size = size
        self._cache = OrderedDict()

    def get(self, key):
        if key in self._cache: # Existing key
            self._cache.move_to_end(key)
            return self._cache[key]
        return -1

    def put(self, key: int, val: int):
        if key in self._cache: # If key already exists update it
            self._cache[key] = val
            self._cache.move_to_end(key)
        else: # New item
            self._cache[key] = val

            if len(self._cache) > self.size:
                self._cache.popitem(last=False)

    def __str__(self):
        items = [f'({k}, {v})' for k, v in self._cache.items()]
        return '{' + ''.join(items) + '}'


if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache)
    print(cache.get(1))
    cache.put(1,1)
    cache.put(2,2)
    print(cache)
    cache.put(3,3)
    print(cache)
    print(cache.get(2))
