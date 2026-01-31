#!/usr/bin/env python

# We will use a combination doubly linked list and hash set to implement LRU cache
# A cache should support faster retrieval and insertion of data prefarably in O(1) time
# A doubly linked list to keep track of order of items.For every item, we need to know what item comes before it, and what after. Traversal should be both ways
# A hash set to support constant time get and put

# An object to represent Link List Node
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'Node({self.key}, {self.val})'

# An object to represent cache
class LRUCache:
    def __init__(self, size: int):
        self.size = size
        # Hash set to items: key->Node(key, val)
        self._cache = {}
        # All our cache items will be linked in btn dummy
        # head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    # Helper functions that rearranges cache items
    def __add_node(self, node: Node):
        # Add a node at the front of list
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def __remove_node(self, node: Node):
        # Removes a node from list
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = None
        node.next = None

    # Main cache operations
    def get(self, key) -> int:
        # Fetches an item by key. Returns key or -1
        # if item does not exist
        if key in self._cache:
            node = self._cache[key]
            self.__remove_node(node)
            self.__add_node(node)
            return node.key
        return -1

    def put(self, key, val):
        # key exists, just update value
        if key in self._cache:
            node = self._cache[key]
            node.val = val
            self.__remove_node(node)
            self.__add_node(node)
        else: # New item
            new_node = Node(key, val)
            self._cache[key] = new_node
            self.__add_node(new_node)

            # If capacity of cache is exceeded, remove
            # least recently used node
            if len(self._cache) > self.size:
                node_to_remove = self.tail.prev
                self.__remove_node(node_to_remove)
                del self._cache[node_to_remove.key]
    
    # Function to display the current state of the cache
    def __str__(self):
        items = []
        for item in self._cache.values():
            items.append(str(item))
        return '{' + ', '.join(items) + '}'

if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache)
    cache.put(1, 1)
    cache.put(2,2)
    print(cache)
    print(cache.get(1))
    print(cache.get(3))
    cache.put(3,3)
    print(cache)
    cache.put(4,4)
    print(cache)
