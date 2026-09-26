class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pallindrome(str1):
            return str1==str1[::-1]
        str1=''
        for i in range(len(s)):
            str1=s[:i]+s[i+1:]
            if pallindrome(str1):
                return True
        return False