"""
Kth Smallest Integer in BST
Link: https://neetcode.io/problems/kth-smallest-integer-in-bst

Difficulty: Medium

Task:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given a binary tree, find and return the K-th smallest integer in it.

            Parameters:
                    root (Optional[TreeNode]): a binary tree
                    k (int): an integer representing the k-th smallest value to find in root

            Returns:
                    int: the value of the k-th smallest integer in root.
        """
        # helper function to perform in-order traversal of root
        # in-order traversal returns nodes in sorted order for BSTs
        def inOrderTraversal(node, vals):
            if not node:
                return
            
            inOrderTraversal(node.left, vals)
            vals.append(node.val)
            inOrderTraversal(node.right, vals)

            return vals
        
        vals = inOrderTraversal(root, [])
        return vals[k - 1]