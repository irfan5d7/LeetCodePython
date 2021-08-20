# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k==0: return head
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length+=1
        k = k % length
        if k == 0: return head
        k = length - k
        temp.next = head
        newHead = head
        while k-1:
            k-=1
            newHead = newHead.next
        prev = newHead
        newHead = newHead.next
        prev.next= None
        return newHead
        
            
        
        