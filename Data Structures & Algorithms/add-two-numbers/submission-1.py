# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        carry=0
        count=0
        head=None
        while temp1 and temp2:
            add=temp1.val+temp2.val
            add+=carry
            if add>9:
                value=add-10
                carry=1
            else:
                value=add
                carry=0
            newNode=ListNode(value)
            if count==0:
                head=newNode
                temp=head

            else:
                temp.next=newNode
                temp=temp.next
            count+=1
            temp1=temp1.next
            temp2=temp2.next
        while temp1:
            add=temp1.val+carry
            if add>9:
                value=add-10
                carry=1
            else:
                value=add
                carry=0
            newNode=ListNode(value)
            temp.next=newNode
            temp=temp.next
            temp1=temp1.next
            count+=1
        while temp2:
            add=temp2.val+carry
            if add>9:
                value=add-10
                carry=1
            else:
                value=add
                carry=0
            newNode=ListNode(value)
            temp.next=newNode
            temp=temp.next
            temp2=temp2.next
            count+=1
        if carry>0:
            newNode=ListNode(carry)
            temp.next=newNode
            temp=temp.next
            count+=1
            carry=0
        return head

