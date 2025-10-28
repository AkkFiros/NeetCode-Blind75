"""
Reorder Linked List
Link: https://neetcode.io/problems/reorder-linked-list

Difficulty: Medium

Task:
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Given the head of a linked list, reorder the nodes of the linked list in-place.

            Parameters:
                    head (Optional[ListNode]): a linked list

            Returns:
                    None::(modifies the linked list in place) 
        """
        # step 1: find middle of head using fast and slow pointers, break list into 2 halves
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        l2 = slow_ptr.next
        slow_ptr.next = None

        # step 2: reverse l2
        prev = None
        curr = l2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev

        # step 3: merge head and l2
        while head and l2:
            head_next = head.next
            l2_next = l2.next

            head.next = l2
            l2.next = head_next

            head = head_next
            l2 = l2_next

        return