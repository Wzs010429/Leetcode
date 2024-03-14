# leetcode 669 修剪二叉搜索树

# 第一种 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


# 第二种 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root

        # 先用一个while把界限控制下来
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
            
        cur = root

        while cur:
            while cur.left and cur.left.val < low:
               cur.left = cur.left.right
            cur = cur.left

        cur = root

        while cur: 
            while cur.right and cur.right.val > high:
               cur.right = cur.right.left
            cur = cur.right


        return root

