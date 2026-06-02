class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maxv=0
        l=0
        res=0
        if not s:
            return 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]]=1
            else:
                count[s[r]]+=1
            maxv=max(count.values())
            lengthA=r-l+1
            if lengthA-maxv>k:
                count[s[l]]-=1
                l+=1
                maxv=max(count.values())
            res=max(res,r-l+1)
        return res
                
