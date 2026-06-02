class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=dict()
        dict2=dict()
        if(len(s)==len(t)):
            for i in range(0,len(s)):
                if s[i] not in dict1:
                    dict1[s[i]]=1
                else:
                    dict1[s[i]]=dict1[s[i]]+1
                if t[i] not in dict2:
                    dict2[t[i]]=1
                else:
                    dict2[t[i]]=dict2[t[i]]+1
            
            if(dict1==dict2):
                return True
            else:
                return False
        return False
        