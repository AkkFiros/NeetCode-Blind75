"""
Remove Node From End of Linked List
Link: https://neetcode.io/problems/remove-node-from-end-of-linked-list

Difficulty: Medium

Task:
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, and an integer n, remove the n-th node from the end of the list.

            Parameters:
                    head (Optional[ListNode]): a linked list
                    n (int): the position from the end of the list

            Returns:
                    Optional[ListNode]: head but with the n-th node from the end removed 
        """
        dummy = ListNode(0, head)
        tracker = dummy
        to_remove = dummy

        for i in range(n + 1):
            tracker = tracker.next

        while tracker:
            tracker = tracker.next
            to_remove = to_remove.next

        to_remove.next = to_remove.next.next

        return dummy.next