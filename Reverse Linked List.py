# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = current2= head
        nextNode = None
        list = []
        while current:
            list.append(current.val)
            current = current.next
            
        for i in reversed(list):
            
            current2.val = i
            current2 = current2.next
            
        return head
            
