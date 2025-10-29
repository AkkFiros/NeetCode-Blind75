"""
Maximum Depth of Binary Tree
Link: https://neetcode.io/problems/depth-of-binary-tree

Difficulty: Easy

Task:
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given a binary tree, return its depth.

            Parameters:
                    root (Optional[TreeNode]): a binary tree

            Returns:
                    int: the depth of root 
        """
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))