class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[0]*(n+1)
        for i in range(n+1):
            output[i]=0;
            n=i
            while(n>0):
                rem=n%2;
                if rem==1:
                    output[i]+=1
                n=n//2
        return output