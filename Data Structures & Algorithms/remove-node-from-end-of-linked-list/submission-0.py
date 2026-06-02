# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        target=count-n+1
        count=0
        prev=None
        cur=head
        while cur:
            count+=1
            if count==target:
                if prev==None:
                    head=head.next
                    return head
                cur=cur.next
                prev.next=cur
                return head
            prev=cur
            cur=cur.next
        return head