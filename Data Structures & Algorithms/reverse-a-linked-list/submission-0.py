# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative version
        # Time - O(n) looping through the while linked list
        # Memory - O(1) not using any data structures, just ptrs
        # Have two pointers, one keeps track of previous node
        # Other pointer keeps track of the current node

        prev, curr = None, head

        # Loop while curr node is not null
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # When loop is completed the prev is set to curr 
        # So prev is the head of the list
        return prev


