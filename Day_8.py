'''Find the Middle Node of a Singly Linked List

Given the head of a singly linked list, find and print the middle node. If there are two middle nodes, print the second middle node.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle = findMiddle(head)

print(middle.data)
