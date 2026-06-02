# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        temp1=list1
        temp2=list2
        temp3=head
        while temp1!=None and temp2!=None:
            if temp1.val>temp2.val:
                if head==None:
                    head=temp2
                    temp3=temp2
                else:
                    temp3.next=temp2
                    temp3=temp3.next
                temp2=temp2.next
            else:
                if head==None:
                    head=temp1
                    temp3=temp1
                else:
                    
                    temp3.next=temp1
                    temp3=temp3.next
                temp1=temp1.next
        
        while temp1!=None:
            if temp3==None:
                head=temp1
                temp3=temp1
            else:
                temp3.next=temp1
                temp3=temp3.next
            temp1=temp1.next
        while temp2!=None:
            if temp3==None:
                head=temp2
                temp3=temp2
            else:
                temp3.next=temp2
                temp3=temp3.next
            temp2=temp2.next
        return head
        