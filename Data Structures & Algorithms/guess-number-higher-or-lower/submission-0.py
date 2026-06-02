# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        begin=1
        end=n
        while begin<=end:
            mid=(begin+end)//2
            value=guess(mid)
            if value>0:
                begin=mid+1
                
            elif value<0:
                end=mid-1
            else:
                return mid