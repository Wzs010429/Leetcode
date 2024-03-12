## Leetcode 654 最大二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            return TreeNode(nums[0])

        maxNum = -1
        maxIndex = -1

        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i

        root = TreeNode(val=maxNum)

        if 0 < maxIndex:
            leftTree = nums[:maxIndex]
            root.left = self.constructMaximumBinaryTree(leftTree)

        if maxIndex < len(nums) - 1:
            rightTree = nums[maxIndex + 1:]
            root.right = self.constructMaximumBinaryTree(rightTree)

        return root
