class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # CHANGED: must use OR, otherwise head.next crashes when head is None
        if head is None or head.next is None:
            return 
        
        slow = head
        fast = head
        
        # CHANGED: standard middle finding
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # CHANGED: split list into two halves
        second = slow.next
        slow.next = None   # IMPORTANT to break the list
        
        # -------- Reverse second half --------
        prev = None
        cur = second
        
        # CHANGED: proper full reverse loop
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        reverseHead = prev
        
        # -------- Merge two halves --------
        first = head
        
        # CHANGED: correct merging logic
        while reverseHead:
            temp1 = first.next
            temp2 = reverseHead.next
            
            first.next = reverseHead
            reverseHead.next = temp1
            
            first = temp1
            reverseHead = temp2
