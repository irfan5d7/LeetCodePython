# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def help(node):
            if node == None:
                return [0,1]
            k = help(node.next)
            s = k[0]+(node.val*k[1])
            return [s,k[1]*2]
        return help(head)[0]
        