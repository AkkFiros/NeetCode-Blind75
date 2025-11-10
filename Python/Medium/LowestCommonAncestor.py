"""
Lowest Common Ancestor in Binary Search Tree
Link: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

Difficulty: Medium

Task:
Given a binary search tree (BST) where all node values are unique, 
and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is 
the lowest node in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Given a binary tree, root, and 2 nodes within it, p and q, find the lowest common ancestor of p and q within root.

            Parameters:
                    root (Optional[TreeNode]): a binary tree
                    p (Optional[TreeNode]): a node within root
                    q (Optional[TreeNode]): a node within root

            Returns:
                    Optional[TreeNode]: The lowest common ancestor of p and q wihtin root 
        """
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
            
"""
Notes:
- Iterative (above) and recursive (below) methods both have O(h) time complexity, where h is height of tree.
- Iterative method has O(1) space complexity, while recursive method has O(h) space complexity due to call stack.
- Recursive method:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
"""