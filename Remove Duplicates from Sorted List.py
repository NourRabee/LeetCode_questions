# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head 
        # This is require to keep track of the prev Node
        prev = None
        dict = {}
        while current:
            
            if current.val not in dict:
                
                dict[current.val] = None
                # Track the prev Node
                prev = current
                
            else:
                # When a duplicate is found assign prev Node's next to current's next
                prev.next = current.next
                
            current = current.next 
            
        return head
