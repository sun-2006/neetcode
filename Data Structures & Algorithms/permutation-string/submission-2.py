class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if s1=='':
            return True
        counts1=dict()
        counts2=dict()
        for i in "abcdefghijklmnopqrstuvwxyz":
            counts1[i]=0
            counts2[i]=0
        for j in range(len(s1)):
            counts1[s1[j]]+=1
            counts2[s2[j]]+=1
        number=0
        for k in "abcdefghijklmnopqrstuvwxyz":
            if counts1[k]==counts2[k]:
                number+=1
        l=0
        r=len(s1)-1
        while number!=26 and r<len(s2):
            counts2[s2[l]]-=1
            if counts2[s2[l]]==counts1[s2[l]]:
                number+=1
            elif counts2[s2[l]]+1==counts1[s2[l]]:
                number-=1
            l+=1
            r+=1
            if r==len(s2):
                continue
            counts2[s2[r]]+=1
            
            if counts2[s2[r]]==counts1[s2[r]]:
                number+=1
                
            elif counts2[s2[r]]-1==counts1[s2[r]]:
                number-=1
        if number==26:
            return True
        return False

            