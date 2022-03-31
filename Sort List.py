# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        i = head
        # j = i.next
        while i is not None:
            l.append(i.val)
            i=i.next
        l = sorted(l)
        i = head
        while i is not None:
            for x in l:
                 i.val = x
                 i=i.next
        return head
