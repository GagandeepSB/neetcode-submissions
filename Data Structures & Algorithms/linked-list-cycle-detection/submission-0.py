# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = {}
        while head:
            if head in check:
                return True
                break
            check[head] = len(check)
            head = head.next
        
        return False