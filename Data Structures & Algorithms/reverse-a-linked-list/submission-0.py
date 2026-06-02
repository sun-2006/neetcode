# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        if head==None or head.next==None :
            return head
        cur=head
        suc=cur.next
        while cur!=None:
            cur.next=prev
            prev=cur
            cur=suc
            if suc!=None:
                suc=suc.next
        head=prev
        return head