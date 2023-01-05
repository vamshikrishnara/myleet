class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        para=[]
        def back(st=[],l=0,r=0):
            if len(st)==2*n:
                para.append("".join(st))
                return
            if l<n:
                st.append("(")
                back(st,l+1,r)
                st.pop()
            if r<l:
                st.append(")")
                back(st,l,r+1)
                st.pop()
        back()
        return para
                
        