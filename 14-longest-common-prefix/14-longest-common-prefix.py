class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=[]
        temp=""
        longest=""
        short=strs[0]
        for i in range(len(strs[0])):
            temp=temp+short[i]
            count=0
            for j in range(1,len(strs)):
                k=strs[j]
                if short[0:i+1]==k[0:i+1]:
                    count=count+1
                else:
                       return longest
                    
            if count==len(strs)-1:
                    longest=temp
            
        return longest
            
        
            