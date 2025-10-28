"""
Merge K Sorted Linked Lists
Link: https://neetcode.io/problems/merge-k-sorted-linked-lists

Difficulty: Hard

Task:
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Given k sorted linked lists, merge all of them into 1 sorted linked list.

            Parameters:
                    lists (list[Optional[ListNode]]): a list of k number of linked lists

            Returns:
                    Optional[ListNode]: a linked list that is the merger of all linked lists in lists 
        """
        
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
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
        
        if not lists:
            return None
        
        merged = lists[0]

        for lst in lists[1:]:
            merged = mergeTwoLists(merged, lst)

        return merged