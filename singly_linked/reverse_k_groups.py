#!/usr/bin/env python

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_k_groups(head: LinkNode, k: int) -> LinkNode:
    if not head or k == 1:
        return head
    # Helper function to get length of list
    def get_length(head):
        curr: LinkNode = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    # Helper function that reverses k nodes
    def reverse_k(start, k) -> LinkNode:
        prev, curr = None, start
        for _ in range(k):
            if not curr:
                return start,None
            next_node = curr.next
            prev = curr
            curr.next = prev
            curr = next_node
        return prev, curr

    length = get_length(head)
    dummy = LinkNode(0)
    dummy.next = head
    prev_group = dummy
    curr = head

    while length >= k:
        # Get newly reversed head and next head to start
        # reversing
        new_head, next_group = reverse_k(curr, k)
        # Link new head to previous group
        prev_group.next = new_head
        # Link old head to next group
        curr.next = next_group
        # Update pointers
        prev_group = curr
        curr = next_group
        length -= k
    return dummy.next

def print_list(head):
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

    # new_head = reverse_k_groups(head, 2)
    #print_list(new_head)
