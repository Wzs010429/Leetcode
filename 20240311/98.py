# leetcode 98 验证二叉搜索树

# 首先是递归法 中序遍历 构建数组

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vec = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec = []
        self.transform(root)

        for i in range(1, len(self.vec)):
            if self.vec[i].val <= self.vec[i - 1].val:
                return False

        return True

    def transform(self, root):
        if not root:
            return

        self.transform(root.left)
        self.vec.append(root)
        self.transform(root.right)


# 另一种递归 记录最小值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minimum = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)

        if root.val > self.minimum:
            self.minimum = root.val
        else:
            return False

        right = self.isValidBST(root.right)

        return left and right