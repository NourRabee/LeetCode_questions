# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        current=head
        previous=None
        
        while current is not None:  
            
            if head is None:
                return None
            
            elif current is None:
                break
                
            elif head.val==val:
                head=head.next
                current=head 
                
            elif current.val==val:
                
                # temp=current.next
                previous.next=current.next
                current = current.next    
                
            else:
                previous=current
                current=current.next
                
        return head
