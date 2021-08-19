# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        bTail = list2
        while bTail.next:
            bTail = bTail.next
        aNode = list1
        count = 0
        while count != a-1:
            count+=1
            aNode=aNode.next
        bNode = aNode
        while count != b:
            count+=1
            bNode = bNode.next
        last = bNode.next
        aNode.next = list2
        bTail.next = last
        return list1
        