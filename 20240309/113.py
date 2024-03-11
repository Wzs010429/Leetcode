# leetcode 113 路经总和 ii

# 首先迭代法秒了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ## 还是先迭代法秒了

        stack = [(root, [root.val])]
        result = []

        while stack:
            node, value = stack.pop()

            if not node.left and not node.right and sum(value) == targetSum:
                result.append(value)

            if node.left:
                stack.append((node.left, value + [node.left.val]))

            if node.right:
                stack.append((node.right, value + [node.right.val]))

        return result

## 来个递归的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.calPath(root, targetSum, [], result)
        return result

    def calPath(self, node, tar, path, result):
        if not node:
            return

        path.append(node.val)

        tar -= node.val
        if not node.left and not node.right and tar == 0:
            result.append(list(path))

        self.calPath(node.left, tar, path, result)
        self.calPath(node.right, tar, path, result)

        path.pop()