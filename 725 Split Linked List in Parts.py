# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            node = node.next
            length+=1
        each, extra = length // k , length % k
        res = [each+1] * extra + [each] * (k- extra)
        output = [None] * k
        prev, curr = None, head
        for indx,num in enumerate(res):
            if prev:
                prev.next = None
            output[indx] = curr
            for i in range(res[indx]):
                prev = curr
                curr = curr.next
        return output