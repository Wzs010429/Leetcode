# leetcode 面试题 02.07 链表相交


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None
        numA, numB = 0, 0

        pointerA, pointerB = headA, headB

        # list1 = [pointerA]

        # while pointerA is not None:
        #     list1.append(pointerA.next)
        #     pointerA = pointerA.next

        # while pointerB is not None:
        #     if pointerB in list1:
        #         return pointerB
        #     else:
        #         pointerB = pointerB.next

        # return None

        while pointerA is not None:
            pointerA = pointerA.next
            numA += 1

        while pointerB is not None:
            pointerB = pointerB.next
            numB += 1

        dis = numA - numB

        pointerA, pointerB = headA, headB

        if dis < 0:
            for _ in range(-dis):
                pointerB = pointerB.next
        else:
            for _ in range(dis):
                pointerA = pointerA.next
        '''
        while pointerA != None:
            if pointerB == pointerA:
                return pointerB
            pointerB = pointerB.next
            pointerA = pointerA.next

        return None
        '''

        while pointerA != pointerB:
            pointerB = pointerB.next
            pointerA = pointerA.next

        return pointerA



