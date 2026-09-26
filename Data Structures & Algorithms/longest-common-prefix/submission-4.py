class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substring=""
        strs.sort()
        if strs[0]=='':
            return ''
        for i in range(len(strs[0])):
            found=1
            for j in range(1,len(strs)):
                if strs[j]=='':
                    return ''
                if strs[0][i]!=strs[j][i]:
                    found=0
                    break
            if found==0:
                break
            else:
                substring+=strs[0][i]
        return substring




        