# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1:
            num1 = (num1 * 10) + l1.val
            l1 = l1.next
        while l2:
            num2 = (num2 * 10) + l2.val
            l2 = l2.next
        num1 += num2
        if num1 == 0:
            return ListNode(num1)
        dummy = ListNode(None)
        while num1:
            node = ListNode(num1%10)
            node.next = dummy.next
            dummy.next = node
            num1 //= 10
        return dummy.next
        