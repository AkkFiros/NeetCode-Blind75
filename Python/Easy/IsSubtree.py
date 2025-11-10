"""
Subtree of Another Tree
Link: https://neetcode.io/problems/subtree-of-a-binary-tree

Difficulty: Easy

Task:
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given 2 binary trees, check if the second is a subtree of the first.

            Parameters:
                    root (Optional[TreeNode]): a binary tree
                    subRoot (Optional[TreeNode]): a binary tree

            Returns:
                    bool: True if subRoot is a subtree of root, False otherwise 
        """
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
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