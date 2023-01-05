class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi=0
        list1=[]
        list1.append(-1)
        for i in range(len(s)):
            if s[i]=='(':
                list1.append(i)
            else:
                list1.pop(-1)
                if len(list1)==0:
                    list1.append(i)
                else:
                    maxi=max(maxi,i-list1[-1])
        return maxi