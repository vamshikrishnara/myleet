class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val=""
        for i in digits:
            val+=str(i)
        val=str(int(val)+1)
        val=list(val)
        return val