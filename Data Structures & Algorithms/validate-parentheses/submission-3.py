class Solution:
    def isValid(self, s: str) -> bool:
        l1=list()
        for i in s:
            if i=='(':
                l1.append(i)
            elif i==')':
                if len(l1)==0 or l1.pop()!='(':
                    return False
            elif i=='{':
                l1.append(i)
            elif i=='}':
                if len(l1)==0 or l1.pop()!='{':
                    return False
            elif i=='[':
                l1.append(i)
            elif i==']':
                if len(l1)==0 or l1.pop()!='[':
                    return False
        if len(l1)!=0:
            return False       
        
        return True

        