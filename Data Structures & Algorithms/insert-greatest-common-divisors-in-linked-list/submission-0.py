# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        
        cur=head
        while cur.next!=None:
            l=ListNode()
            v1=cur.val
            v2=cur.next.val
            valuegcd=gcd(v1,v2)
            l.val=valuegcd
            l.next=cur.next
            cur.next=l
            cur=l.next
        return head
        