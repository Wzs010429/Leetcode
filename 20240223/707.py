# leetcode 707 设计链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.index = 0
        self.dummy_head = ListNode()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.index:
            return -1

        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val=val, next=self.dummy_head.next)
        self.index += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while (cur.next != None):
            cur = cur.next
        cur.next = ListNode(val=val, next=None)
        self.index += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.index:
            return

        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.index += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.index:
            return
        self.index -= 1
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)