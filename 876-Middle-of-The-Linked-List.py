# Date: 08/21/2023
# Leetcode no. 876 - Middle of the Linked List
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Approach:

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pointer = head
    nodes = 0 
    steps = 0
    while pointer.next:
        nodes += 1
        pointer = pointer.next 

    nodes += 1
    steps = nodes // 2 
    while steps > 0:
        head = head.next 
        steps -= 1 
    return head  

if __name__ == "__main__":
    
    # test case 1
    # expected output: [3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(middleNode(head))

    # test case 2
    # expected output: [4,5,6]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(middleNode(head))
