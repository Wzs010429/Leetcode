# leetcode 112 路径总和

## 首先写的是简单的迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # 首先迭代法：
        if not root:
            return False


        res = [root.val]
        stack = [root]

        while stack:
            node = stack.pop()
            val = res.pop()

            if not node.left and not node.right:
                if val == targetSum:
                    return True

            if node.left:
                stack.append(node.left)
                res.append(node.left.val + val)

            if node.right:
                stack.append(node.right)
                res.append(node.right.val + val)

        return False


# 然后看递归法是怎么写的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and targetSum == root.val:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

