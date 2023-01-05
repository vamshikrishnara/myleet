class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastword=""
        l=0
        for i in range(len(s)):
            if s[i]==" ":
                if len(lastword)!=0:
                    l=len(lastword)
                    lastword=""
            else:
                lastword+=s[i]
        if len(lastword)==0:
            return l
        return len(lastword)
        