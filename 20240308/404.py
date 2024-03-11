# leetoce 404 左叶子之和


## 第一种递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        leftSum = self.sumOfLeftLeaves(root.left)
        rightSum = self.sumOfLeftLeaves(root.right)

        if root.left and not root.left.left and not root.left.right:
            leftSum = root.left.val

        res = leftSum + rightSum

        return res


## 第二种 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        res = 0

        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res

