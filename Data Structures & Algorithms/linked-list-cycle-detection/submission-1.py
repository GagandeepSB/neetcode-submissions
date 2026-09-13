# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time - O(n) looping n times
        # Memory - O(1) just using two ptrs
        slow, fast = head, head # Start slow and fast at same positions

        while fast and fast.next: # Check to see if fast and fast.next is not null 
            slow = slow.next # Increment slow by 1
            fast = fast.next.next # Increment fast by 2

            if slow == fast: # If there is a cycle fast will catch up and slow and fast will point to the same node
                return True # If they are equal a cycle exists and return True

        return False # If fast or fast.next are null then there is not a cycle