# leetcode 203 移除列表元素

# 这题就是一个基础题目 主要了解链表是怎么用的

# 链表的基本表达格式

# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 首先定义一个虚拟节点头
        # 虚拟节点头的主要意义在于防止第一个节点就是一个需要被删除的节点
        listnode = ListNode(next = head)

        head = listnode
        # 递归 找到最深处
        while(head.next != None):
            if(head.next.val == val):
                head.next = head.next.next
            else:
                head = head.next
        return listnode.next