# leetcode 94 二叉树的中序遍历


## 第一种 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right = self.inorderTraversal(root.right)
        left = self.inorderTraversal(root.left)

        return left + [root.val] + right


## 第二种 迭代法


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        res = []
        pointer = root

        while stack or pointer:
            if pointer:
                stack.append(pointer)
                pointer = pointer.left
            else:
                pointer = stack.pop()
                res.append(pointer.val)
                pointer = pointer.right

        return res



