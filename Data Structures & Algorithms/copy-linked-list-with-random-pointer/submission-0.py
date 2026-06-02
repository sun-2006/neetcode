class Solution:
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Fix 1: nested function should not have self
        def copyNode(node):
            return Node(node.val)   # Fix 2: pass value
        
        if not head:
            return head
        
        dict1 = {}
        
        temp1 = head
        temp3 = copyNode(temp1)
        temp2 = temp3
        
        # Fix 3: map original -> copy
        dict1[temp1] = temp2
        
        temp1 = temp1.next
        
        # First pass: copy next pointers
        while temp1:
            temp2.next = copyNode(temp1)
            temp2 = temp2.next
            
            dict1[temp1] = temp2  # correct mapping
            
            temp1 = temp1.next
        
        # Second pass: copy random pointers
        temp4 = temp3
        temp5 = head
        
        while temp4:
            if temp5.random:
                temp4.random = dict1[temp5.random]  # use original node
            else:
                temp4.random = None
            
            temp4 = temp4.next
            temp5 = temp5.next
        
        return temp3