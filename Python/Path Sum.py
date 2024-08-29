# Link to the exercise : https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

############### EXERCISE ###############
########################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if (root is None):  # check if tree / subtree is Empty
            return False

        if root.left is None and root.right is None:    # once we reach a leaf node, boolean to return if the sum is equal to target or not
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)    # if a path to a leaf returns the target sum then this line will return true, if not then false
        