class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.strip().lower()
        l=0
        r=len(s1)-1
        while(l<r):
            if(s1[l].isalnum() and s1[r].isalnum()):
                if(s1[l]!=s1[r]):
                    return False
            elif s1[l].isalnum()==False:
                l+=1
                continue
            elif s1[r].isalnum()==False:
                r-=1
                continue
            else:
                l+=1
                r-=1
            l+=1
            r-=1
        return True
