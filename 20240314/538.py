# leetcode 538 把二叉搜索树转换为累加树


# 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.transpose(root)
        return root
    
    def transpose(self, root):
        if not root:
            return None

        self.transpose(root.right)
        root.val += self.pre
        self.pre = root.val
        self.transpose(root.left)

    
# 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += self.pre
                self.pre = cur.val
                cur = cur.left
            
        return root