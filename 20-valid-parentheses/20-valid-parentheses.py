class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        map={")":"(", "}":"{","]":"["}
        for i in s:
            if i in map:
                k=a.pop() if len(a) else '#'
                if k=='#' or map[i]!=k:
                    return False
            else:
                a.append(i)
        if len(a)!=0:
            return False
        return True
                
                    