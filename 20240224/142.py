# leetcode 142 环形列表 2 medium


# 第一种方法是双指针防范

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        quick, slow = head, head

        # 判断两个指针碰撞的条件 一定是首先考虑quick本身和quick的next，因为一次跳两个格子

        # 这块总结出来的经验就是 如果head开头 那么我们就要关注本身而不是从next开始
        while quick is not None and quick.next is not None:
            # slow迭代一个格子 quick迭代两个
            slow = slow.next
            quick = quick.next.next

            if quick == slow:
                slow = head
                # 此刻两个指针重合的地方到环的交点，与从head出发到环的交点，距离是一样的
                # 所以只需要判断出来他俩什么时候相交就可以了
                while slow != quick:
                    slow = slow.next
                    quick = quick.next

                return quick

        return None




# 第二种方法是py的集合法 不断从head节点深入并且保存每一个链表中的节点，如果遇到相同的那么就说明是有一个环

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()

        while head:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return head
        return None