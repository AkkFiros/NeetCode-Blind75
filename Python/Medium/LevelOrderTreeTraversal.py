"""
Binary Tree Level Order Traversal
Link: https://neetcode.io/problems/level-order-traversal-of-binary-tree

Difficulty: Medium

Task:
Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Given a binary tree, return the level order traversal of it.

            Parameters:
                    root (Optional[TreeNode]): a binary tree

            Returns:
                    list[list[int]]: The level order traversal of root as a list of sublists, 
                                     where each sublist contains the values of nodes at the same level.
        """
        res = []

        if not root:
            return res
        
        queue = [root]

        while queue:
            lvl_num_nodes = len(queue)
            curr_lvl = []

            for i in range(lvl_num_nodes):
                this_node = queue.pop(0)
                curr_lvl.append(this_node.val)

                if this_node.left:
                    queue.append(this_node.left)
                
                if this_node.right:
                    queue.append(this_node.right)

                if i == lvl_num_nodes - 1:
                    res.append(curr_lvl)
            
        return res