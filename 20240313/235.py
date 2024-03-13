# leetcode 235 二叉搜索树的最近公共祖先

## 首先递归法秒了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor(root.left, p, q)
            if root:
                return root
            
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p, q)
            if root:
                return root
            
        else:
            return root
        


# 写一个迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left

            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root
        

        