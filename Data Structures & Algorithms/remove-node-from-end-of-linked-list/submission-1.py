class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        for _ in range(n):
            r = r.next
            
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next
        
        return dummy.next