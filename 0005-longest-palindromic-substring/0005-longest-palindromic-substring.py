class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        long=""
        for i in range(len(s)):
            j=len(s)-1
            while j>=i:
                if s[i]==s[j]:
                    temp=s[i:j+1]
                    if temp==temp[::-1] and len(temp)>len(long):
                        long=temp
                        
                j-=1
        return long
                    