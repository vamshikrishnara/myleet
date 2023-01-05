class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        maxi=0
        wc=Counter()
        while right<len(s):
            wc[s[right]]+=1
            while wc[s[right]]>1:
                wc[s[left]]-=1
                left+=1
            right+=1
            maxi=max(maxi,right-left)    
        return maxi
            
                
            