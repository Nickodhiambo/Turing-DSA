#!/usr/bin/env python

# We are looping tnrough both lists simultaneously, extraxt and add up values, handling any carry
# Loop only stops when both lists are exhausted, or there isno carry
# With every run through the loop we add the sum of the current additions as a node at the end of a new link list
# We return the head of the summation link list

# Node of Link List representation
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head: Node) -> Node:
    if not head:
        return None
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def add_two_numbers(l1: Node, l2: Node) -> Node:
    carry = 0
    dummy = Node(0)
    curr = dummy

    #ll1 = reverse_linked_list(l1)
    #ll2 = reverse_linked_list(l2)
    
    while l1 or l2 or carry:
        x1 = l1.val if l1 else 0
        x2 = l2.val if l2 else 0
        total = x1 + x2 + carry
        digit = total % 10
        carry = total // 10

        # Create a node with val digit
        curr.next = Node(digit)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

def print_list(head: Node):
    curr = head
    while curr:
        print(curr.val, end='->')
        curr = curr.next
    print('None')

if __name__ == '__main__':
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    print_list(l1)
    print_list(l2)

    print_list(reverse_linked_list(l1))
    print_list(reverse_linked_list(l2))

    print_list(add_two_numbers(l1, l2))
