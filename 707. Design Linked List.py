class Node:
    def __init__ (self,val = 0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index>= self.size:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
            temp.next = node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return None
        if index == 0:
            self.addAtHead(val)
        elif index == self.size :
            self.addAtTail(val)
        else:
            node = Node(val)
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or self.size == 0:
            return None
        self.size -= 1
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)