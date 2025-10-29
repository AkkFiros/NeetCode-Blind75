"""
Same Binary Tree
Link: https://neetcode.io/problems/same-binary-tree

Difficulty: Easy

Task:
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given two binary trees, check if they are the same tree.

            Parameters:
                    p (Optional[TreeNode]): the first binary tree
                    q (Optional[TreeNode]): the second binary tree

            Returns:
                    bool: True if p and q are the same trees, False otherwise 
        """
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)