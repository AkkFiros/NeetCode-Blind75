"""
Merge Two Sorted Linked Lists
Link: https://neetcode.io/problems/merge-two-sorted-linked-lists

Difficulty: Easy

Task:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the heads of two sorted linked lists, merge them into 1 sorted linked list.

            Parameters:
                    list1 (Optional[ListNode]): the head of the first linked list
                    list2 (Optional[ListNode]): the head of the second linked list

            Returns:
                    Optional[ListNode]: The head of the merged linked list
        """

        ptr1 = list1
        ptr2 = list2

        res = ListNode()

        res_ptr = res

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val >= ptr2.val:
                    res_ptr.next = ptr2
                    ptr2 = ptr2.next
                else:
                    res_ptr.next = ptr1
                    ptr1 = ptr1.next
            elif ptr1:
                res_ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                res_ptr.next = ptr2
                ptr2 = ptr2.next
            
            res_ptr = res_ptr.next

        return res.next