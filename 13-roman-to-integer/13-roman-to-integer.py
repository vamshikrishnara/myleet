class Solution:
    def romanToInt(self, s: str) -> int:
        ri={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        maxi=0
        val=0
        for i in range(len(s)-1,-1,-1):
            if maxi<=ri[s[i]]:
                val+=ri[s[i]]
                maxi=ri[s[i]]
            else:
                val-=ri[s[i]]
        return val