class ListNode:
    def __init__ (self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = None
        self.last = None
        self.max_size = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size == self.max_size:
            return False
        if self.size == 0:
            self.head = ListNode(value)
            self.head.next = self.head
            self.last = self.head
            self.head.prev = self.head
        else:
            node = ListNode(value)
            node.next = self.head
            node.prev = self.last
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size == self.max_size:
            return False
        if self.size == 0:
            self.head = ListNode(value)
            self.head.next = self.head
            self.last = self.head
            self.head.prev = self.head
        else:
            self.last.next = ListNode(value)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.last.next = self.head
            self.head.prev = self.last
        self.size +=1
        return True
    
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.head = self.head.next
        self.head.prev = self.last
        self.last.next = self.head 
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.last = self.last.prev
        self.last.next = self.head
        self.head.prev = self.last
        self.size -= 1
        return True
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size:
            return self.head.val
        return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size:
            return self.last.val
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.size 

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()