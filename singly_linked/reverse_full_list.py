#!/usr/bin/env python

class LinkNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def reverse_linked_list(head: LinkNode) -> LinkNode:
    prev, curr = None, head

    while curr:
        # Reverse links
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

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
    new_head = reverse_linked_list(head)
    print_list(new_head)
