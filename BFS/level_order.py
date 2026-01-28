#!/usr/bin/env python

# We use a queue to store the level under processing
# We loop through the queue, pop an element and add it to
# the current level list
# After all nodes of a level are exhausted, we add the current level list to an output list

from collections import deque
# Create a tree node representation
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def level_order(root: Node) -> list[list[int]]:
    # Edge case: Empty tree
    if not root:
        return []

    # Queue to current level
    queue = deque([root])
    # Output list to store all levels
    result = []

    while queue: # While there are still nodes to process
        current_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(level_order(root))

