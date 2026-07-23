class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(i,o,c,s):
            if i==n*2:
                res.append(s)
                return 
            if o>0:
                backtrack(i+1,o-1,c,s+'(')
            
            if c>o:
                backtrack(i+1,o,c-1,s+')')
            
        backtrack(0,n,n,'')
        return res