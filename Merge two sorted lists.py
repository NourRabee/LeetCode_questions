# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
            l3 = ListNode()
            node = l3
            
            while l1 is not None and l2 is not None:
                
                if l1.val < l2.val:
                    node.next = l1
                    node = node.next
                    l1 = l1.next
                    
                else:
                    node.next = l2
                    node = node.next
                    l2 = l2.next
                    
            if l1 is not None:
                 node.next = l1

            else:
                 node.next = l2
            
            return l3.next
