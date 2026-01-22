#!/usr/bin/env python
# To reverse in groups of K, we need to have two functions;
# One that takes the node to start the reversal from and
# returns the newly reversed head, and the head of the next
# k group to reverse
# The other function should perform the linking of reversed parts to ensure continuity of the linked list

class LinkNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def reverse_k_groups(head: LinkNode, k: int) -> LinkNode:
    # edge case: empty list or k = 1
    if not head or k == 1:
        return head
    # Helper function to calculate length of list
    def get_length(head) -> int:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    # Function that reverses k nodes given starting node
    def reverse_k_nodes(start: LinkNode, k):
        prev, curr = None, start
        for _ in range(k):
            if not curr:
                return start, None
            # Reverse links
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev, curr

    # Link reversed segment with rest of linked list
    length = get_length(head)
    dummy = LinkNode(0)
    dummy.next = head
    prev_group = dummy
    curr = head

    while length >= k: # We stop when remaining nodes are less than k
        new_head, next_group = reverse_k_nodes(curr, k)
        # Link with previous group
        prev_group.next = new_head
        # Link with next group
        curr.next = next_group
        # Update pointers
        prev_group = curr
        curr = next_group
        length -= k
    return dummy.next

# Helper function to print a linked list given head
def print_list(head: LinkNode):
    curr = head
    while curr:
        print(curr.val, end='->')
        curr = curr.next
    print('None')

if __name__ == '__main__':
    head = LinkNode(1)
    head.next = LinkNode(2)
    head.next.next = LinkNode(3)
    head.next.next.next = LinkNode(4)
    print_list(head)

    new_head = reverse_k_groups(head, 2)
    print_list(new_head)

