# leetcode 24 两两交换链表中的节点 medium


# 第一种写法是双指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 双指针写法

        # 定义一个虚拟头节点
        dummyHead = ListNode(next=head)

        # 异常判定
        if head is None or head.next is None:
            return head

        cur = dummyHead

        while cur.next and cur.next.next:
            tmp = cur.next  # 保存1节点
            cur.next = cur.next.next  # 0连接到2
            tmp.next = cur.next.next  # 1连到3
            cur.next.next = tmp  # 2连到1
            cur = tmp

        return dummyHead.next


# 下面是递归的方法 相对来讲也比较简单

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 这种方法是递归的方法
        # 首先判断是否有两个节点可以进行交换
        if not head or not head.next:
            return head

        newHead = head.next # 记录2节点
        head.next = self.swapPairs(newHead.next) # 1节点要链接到后面3节点 需要递归
        newHead.next = head # 2连接到1

        return newHead
