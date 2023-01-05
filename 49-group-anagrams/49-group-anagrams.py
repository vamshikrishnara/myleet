class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        out=[]
        for i in range(len(strs)):
            val=[0]*26
            s=strs[i]
            for j in s:
                val[ord(j)-ord('a')]+=1
            p=str(val)
            ana[p].append(s)
        for k in ana:
            out.append(ana[k])
        return out
            
            