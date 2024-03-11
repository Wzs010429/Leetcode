# leetcode 257 二叉树的所有路径

# 第一种 回溯递归法


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        path = ""
        result = []

        self.getPath(root, result, path)

        return result

    def getPath(self, root, result, path):

        # 这个函数是是用来进行回溯递归的
        path += str(root.val)

        if not root.left and not root.right:
            result.append(path)

        if root.left:
            self.getPath(root.left, result, path + "->")
        if root.right:
            self.getPath(root.right, result, path + "->")

        return




## 接下来用的是迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        path = [str(root.val)]

        stack = [root]

        while stack:
            node = stack.pop()
            tmpPath = path.pop()

            if not node.left and not node.right:
                result.append(tmpPath)

            if node.right:
                stack.append(node.right)
                path.append(tmpPath + "->" + str(node.right.val))

            if node.left:
                stack.append(node.left)
                path.append(tmpPath + "->" + str(node.left.val))

        return result