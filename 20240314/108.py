# leetcode 108 将有序数组转化为二叉搜索树


# 第一种 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.list2BST(nums, 0, len(nums)-1)

    

    def list2BST(self, nums, low, high):
        if low > high:
            return None
        
        mid = low + (high - low) // 2

        root = TreeNode(nums[mid])
        root.left = self.list2BST(nums, low, mid-1)
        root.right = self.list2BST(nums, mid+1, high)

        return root

