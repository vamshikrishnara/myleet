class Solution:
    def myAtoi(self, s: str) -> int:
        val=""
        i=0
        sign=1
        if len(s)==0:
            return 0
        while i<len(s):
            if s[i]!=" ":
                break
            i+=1
        if i< len(s) and s[i]=='-':
            sign=-1
            i=i+1
        elif i<len(s) and s[i]=='+':
            sign=1
            i=i+1
        a=["0","1","2","3","4","5","6","7","8","9"]
        for j in range(i,len(s)):
            if s[j] in a:
                val+=s[j]
            else:
                break
        if len(val)==0:
            return 0
        new_val=sign*int(val)
        if new_val<= -1*(2**31):
            return -1*(2**31)
        elif new_val>=(2**31)-1:
            return (2**31)-1
        else:
            return new_val
            
        