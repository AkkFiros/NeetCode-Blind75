"""
Invert Binary Tree
Link: https://neetcode.io/problems/invert-a-binary-tree

Difficulty: Easy

Task:
You are given the root of a binary tree root. Invert the binary tree and return its root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given a binary tree, invert it and return its root.

            Parameters:
                    root (Optional[TreeNode]): a binary tree

            Returns:
                    Optional[TreeNode]: root after inversion 
        """
        if root == None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root