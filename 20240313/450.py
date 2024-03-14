# leetcode 450 删除二叉搜索树中的节点

## 首先是迭代法

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
        cur = root
        pre = None
        while cur:          
            if cur.val > key:
                pre = cur
                cur = cur.left
            elif cur.val < key:
                pre = cur
                cur = cur.right
            else:
                break
        # 直接删除头节点 因为pre还没有便利
        if not pre:
            return self.deleteOneNode(root)

        if pre.left and pre.left.val == key:
            pre.left = self.deleteOneNode(cur)

        if pre.right and pre.right.val == key:
            pre.right = self.deleteOneNode(cur)

        return root


    def deleteOneNode(self, node):
        if not node:
            return node
        # 没有左子树没有右子树 直接删
        elif not node.left and not node.right:
            return None
        # 删除节点还有左子树没有右子树 把左子树的第一个节点接过来
        elif not node.right and node.left:
            return node.left
        # 删除节点还有右子树没有左子树 把右子树的第一个节点接过来
        elif not node.left and node.right:
            return node.right
        # 有左子树和右子树 把左子树放在右子树的最左下节点 右子树第一个接过去
        else:
            tmp = node.right
            while tmp.left:
                tmp = tmp.left
            tmp.left = node.left

            return node.right

        
        

        