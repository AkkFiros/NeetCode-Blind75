"""
Reverse Linked List
Link: https://neetcode.io/problems/reverse-a-linked-list

Difficulty: Easy

Task:
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, reverse the list and return the new head.

            Parameters:
                    head (Optional[ListNode]): the head of a linked list

            Returns:
                    Optional[ListNode]: The head of the reversed linked list
        """

        pointer = head
        prev = None

        while pointer:
            next_node = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next_node

        return prev