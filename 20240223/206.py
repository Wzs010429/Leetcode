# 206 反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        # 这块为什么是cur而不是cur.next 踩坑了

        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev