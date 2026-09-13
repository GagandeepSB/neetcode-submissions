# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a node to begin the list
        # Prevents from inserting into an empty LL, mergedList is a dummy node
        mergedList = ListNode()
        # mergedList.next points to the head of the list
        tail = mergedList # Holds the tail of the list

        # Iterate while both of them are non empty
        # Can only compare when the lists are not empty
        while list1 and list2:
            if list1.val < list2.val: # If list1 val is less than list2 val
                tail.next = list1 # Insert the node
                list1 = list1.next # Move to the next node in list1

                # list2 val is less than list1 val
            else: 
                tail.next = list2
                list2 = list2.next

            # Move tail to the next node
            tail = tail.next

        # Once we have reached this the loop has terminated
        # The loop has terminated since list1 or list2 or both are null
        # If list1 is not null then we make tail.next point to the current l1 node
        # This connects the rest of the l1 nodes to our mergedList as well
        # Same goes for l2, l2 exectues when l1 is null 
        # l1 executes when l2 is null
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Returning the head of the linked list
        # mergedList is a dummy node, so head of the list is at mergedList.next 
        return mergedList.next