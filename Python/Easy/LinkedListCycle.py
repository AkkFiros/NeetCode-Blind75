"""
Linked List Cycle Detection
Link: https://neetcode.io/problems/linked-list-cycle-detection

Difficulty: Easy

Task:
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists.
The tail node of the list will set it's next pointer to the index-th node.
If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a linked list, determine if there is a cycle in it.

            Parameters:
                    head (Optional[ListNode]): the head of a linked list

            Returns:
                    bool: True if there is a cycle in the linked list, False otherwise.
        """

        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
            
        return False