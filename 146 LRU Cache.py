class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.last = None
        self.size = 0
        self.mp = {}
    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        res = self.mp[key]
        self.put(key,res.val)
        return res.val
        

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key in self.mp:
            self.size -= 1
            nod = self.mp[key]
            if nod == self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.last = None
            elif nod == self.last:
                self.last =self.last.prev
                self.last.next = None
            else:
                nod.prev.next = nod.next
                nod.next.prev = nod.prev
            self.mp.pop(key)
        if self.size == self.capacity:
            ky = self.head.key
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.last = None
            self.size -= 1
            self.mp.pop(ky)
        if self.size == 0:
            self.head = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = self.last.next
        self.size +=1
        self.mp[key] = node
            
                    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)