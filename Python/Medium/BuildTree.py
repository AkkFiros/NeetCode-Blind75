"""
Construct Binary Tree from Preorder and Inorder Traversal
Link: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal

Difficulty: Medium

Task:
You are given two integer arrays preorder and inorder.

• preorder is the preorder traversal of a binary tree
• inorder is the inorder traversal of the same tree
• Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Given a preorder and inorder traversals of a tree, construct and return the tree.

            Parameters:
                    preorder (list[int]): the preorder traversal of a binary tree
                    inorder (list[int]): the inorder traversal of the same binary tree

            Returns:
                    Optional[TreeNode]: a binary search tree constructed from preorder and inorder.
        """
        if not preorder or not inorder:
            return None
        
        # construct dictionary of indices of values for inorder traversal
        inorder_indices = {}
        for i in range(len(inorder)):
            inorder_indices[inorder[i]] = i

        # initialise preorder index (for root of subtrees)
        # keeps track of current root when building tree
        self.preorder_index = 0

        # helper function to build tree recursively using inorder indices:
        # left and right are the bounds of the current subtree in inorder traversal
        # preorder array only used to determine root values
        def builder(left, right):
            if left > right:
                return None
            
            # get root value from preorder
            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            
            # increment preorder_index for next call
            self.preorder_index += 1

            # build left and right subtrees
            mid = inorder_indices[root_val]
            root.left = builder(left, mid - 1)
            root.right = builder(mid + 1, right)

            return root
        
        return builder(0, len(inorder) - 1)
"""
Notes:
- Above shows optimal solution with O(n) time and space complexities.
- O(n) time complexity since dictionary reduces list splicing.
- Below is intuitive but less optimal solution:
  class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # first element in preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # find the index of the root in inorder
        root_index_inorder = inorder.index(root_val)

        # elements to the left of root_index_inorder in inorder are part of the left subtree
        # elements to the right of root_index_inorder in inorder are part of the right subtree
        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1 :]

        # correspond elements in preorder for left and right subtrees using left_inorder and right_inorder lengths
        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # build tree
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
- Less optimal solution has O(n^2) time complexity due to list splicing and index() calls.
"""