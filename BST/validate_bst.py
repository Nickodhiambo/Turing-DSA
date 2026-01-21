#! /usr/bin/env python

# Start from the root node use range based searching to
# search the entire left subtree, then right subtree
# Recursively search subtrees on both left and right

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def validate_bst(root: Node) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            # An empty BST is still a valid BST
            return True
        # Check if value of a node is outside range
        if node.val <= min_val or node.val >= max_val:
            return False
        # Recursively check left and right subtrees of every node on left and right of root
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    # start from root
    return validate(root, float('-inf'), float('inf'))

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(7)
    root.right = Node(13)
    root.left.left = Node(5)
    root.left.right = Node(8)
    root.right.left = Node(11)
    root.right.right= Node(15)

    print(validate_bst(root))
