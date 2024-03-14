# leetcode 701 二叉搜索树中的插入操作

## 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            node = TreeNode(val)
            return node
        
        cur = root
        pre = root

        while cur:
            pre = cur
            if val > cur.val:       
                cur = cur.right
            else:
                cur = cur.left

        node = TreeNode(val=val)
        if pre.val < val:
            pre.right = node
        else:
            pre.left = node

        return root
            

## 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val=val)
            return node
        
        self.pre = TreeNode(0)
        self.trans(root, val)

        return root

        
    
    def trans(self, root, val):
        if not root:
            node = TreeNode(val=val)

            if val > self.pre.val:
                self.pre.right = node
            else:
                self.pre.left = node
            
            return
        
        self.pre = root
        if val > root.val:
            self.trans(root.right, val)
        if val < root.val:
            self.trans(root.left, val)
        


## 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.right and not root.left:
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            else:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                tmp.left = root.left
                return root.right
        
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root




