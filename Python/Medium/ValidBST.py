"""
Valid Binary Search Tree
Link: https://neetcode.io/problems/valid-binary-search-tree

Difficulty: Medium

Task:
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:
• The left subtree of every node contains only nodes with keys less than the node's key.
• The right subtree of every node contains only nodes with keys greater than the node's key.
• Both the left and right subtrees are also binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, check if it is a valid binary search tree.

            Parameters:
                    root (Optional[TreeNode]): a binary tree

            Returns:
                    bool: True if root is a valid binary search tree, False otherwise.
        """
        
        # helper function to ensure that all child nodes of a given node
        # remain within the valid val range (set by parent node(s))
        def valTracker(node, low, high):
            if not node:
                return True
            
            if not (low < node.val <high):
                return False
            
            return valTracker(node.left, low, node.val) and valTracker(node.right, node.val, high)
        
        return valTracker(root, -float('inf'), float('inf'))