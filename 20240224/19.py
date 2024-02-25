# leetcode 19 删除列表的倒数第N个节点 medium


# 第一种做法，先统计出来有多少个节点，然后计算删除节点的位置进行删除

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummyHead = ListNode(next=head)

        num = 0  # 统计链表中有多少个节点

        cur = dummyHead
        while cur.next is not None:
            cur = cur.next
            num += 1

        index = num - n  # 需要删除的节点的位置的前一个节点 不是index 就是单纯的计数

        cur = dummyHead
        for _ in range(index):
            cur = cur.next

        cur.next = cur.next.next


# 下面的方法是用栈的思想去解决问题

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 用栈的思想去解决问题

        dummyHead = ListNode(next=head)

        stack = list()
        cur = dummyHead
        while cur:
            stack.append(cur)
            cur = cur.next

        # 把需要被删除的节点和后面的节点全部都删除
        for _ in range(n):
            stack.pop()

        # 找到被删除节点的前一个节点
        front = stack[-1]

        front.next = front.next.next

        return dummyHead.next


# 接下来用双指针去做这个题目

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 这次用双指针来做这个题目

        # 首先定义虚拟头节点和双指针
        dummyHead = ListNode(next=head)
        quick = dummyHead
        slow = dummyHead
        dis = 0
        # 让 quick 指针先走 n+1 步
        for _ in range(n + 1):
            quick = quick.next

        # 然后 quick 和 slow 一起走，直到 quick 指向链表末尾
        while quick:
            quick = quick.next
            slow = slow.next
        slow.next = slow.next.next

        return dummyHead.next