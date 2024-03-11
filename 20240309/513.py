# leetcode 513 找树左下角的值


# 第一种 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # 先把迭代的方法写出来

        if not root:
            return None

        queue = collections.deque([root])
        res = -1

        while queue:
            node = queue.popleft()
            res = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return res



## 第二种 看一下递归怎么写

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth = -1
        self.result = None
        self.getValue(root, 0)
        return self.result

    def getValue(self, node, depth):

        if not node.left and not node.right:
            if depth > self.depth:
                self.result = node.val
                self.depth = depth
            return

        if node.left:
            self.getValue(node.left, depth + 1)

        if node.right:
            self.getValue(node.right, depth + 1)


