class ListNode:
    def __init__ (self,val = None,next = None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.head = None
        self.last = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        node = ListNode(value)
        if self.size == 0:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next
            self.last.next = self.head
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.head = None
            self.last = None
        else:
            self.head = self.head.next
            self.last.next = self.head
        self.size -= 1
        return True
    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.last.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size==self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()