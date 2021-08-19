class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
        
class FrontMiddleBackQueue:

    def __init__(self):
        self.head = None
        self.last = None

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.last.next = self.head

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
            return
        if self.head.next == self.head:
            node.next = self.head
            node.prev = self.last
            self.head.prev = node
            self.head = node
            self.last.next = self.head
            return
        front = self.head
        last = self.last
        while front != last and front.next != last :
            front=front.next
            last = last.prev
        if front == last:
            front = front.prev
        front.next = node
        node.prev = front
        node.next = last
        last.prev = node
            

    def pushBack(self, val: int) -> None:
        node = Node(val)
        if self.last == None:
            self.head = node
            self.last = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.last
            self.last.next = node
            self.last = node
            self.head.prev = self.last
        

    def popFront(self) -> int:
        if self.head == None:
            return -1
        val = self.head.val
        if self.head.next == self.head:
            self.head = None
            self.last = None
            return val
        self.head = self.head.next
        self.last.next = self.head
        self.head.prev = self.last
        return val
        
    def popMiddle(self) -> int:
        if self.head == None:
            return -1
        if self.head.next == self.head:
            val = self.head.val
            self.head = None
            self.last = None
            return val
        front = self.head
        last = self.last
        while front != last and front.next != last :
            front=front.next
            last = last.prev
        val = front.val
        if front == last:
            last = last.next
        if front == self.head:
            front = front.next
            self.head = front
            front.prev = self.last
            self.last.next = self.head 
        else:
            front = front.prev
            front.next = last
            last.prev = front
        return val
            
        
        

    def popBack(self) -> int:
        if self.last == None:
            return -1
        val = self.last.val
        if self.last.next == self.last:
            self.head = None
            self.last = None
            return val
        self.last = self.last.prev
        self.last.next = self.head
        self.head.prev = self.last
        return val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()