# leetcode 530 二叉搜索树的最小绝对差


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vec = []

    def transform(self, root):
        if not root:
            return

        self.transform(root.left)
        self.vec.append(root)
        self.transform(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec = []
        self.transform(root)
        res = float('Inf')
        for i in range(1, len(self.vec)):
            if abs(self.vec[i].val - self.vec[i - 1].val) < res:
                res = abs(self.vec[i].val - self.vec[i - 1].val)

        return res


# 写一下迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # 写一下迭代法

        stack = []
        cur = root
        pre = None
        result = float('inf')

        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)  # 将访问的节点放进栈
                cur = cur.left  # 左
            else:
                cur = stack.pop()
                if pre is not None:  # 中
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right  # 右

        return result


