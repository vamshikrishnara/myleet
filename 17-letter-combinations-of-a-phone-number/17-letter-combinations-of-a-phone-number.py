class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lc={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return list(lc[digits[0]])
        else:
            out=list(lc[digits[0]])
            for i in range(1,len(digits)):
                l1=list(lc[digits[i]])
                temp=[]
                for j in range(len(out)):
                    for k in range(len(l1)):
                        temp.append(out[j]+l1[k])
                out=temp
            return out
            