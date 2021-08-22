# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0 : return None
        if n == 1: return lists[0]
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue(maxsize = n)
        for indx, elem in enumerate(lists):
            if elem: q.put((elem.val,indx,elem))
        while q.qsize():
            node = q.get()
            curr.next = node[2]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val,node[1],curr.next))
        return dummy.next
        
        
        