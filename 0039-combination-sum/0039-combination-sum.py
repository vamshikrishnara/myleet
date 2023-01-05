class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def bctk(candies,sub,rst):
            if rst==0:
                if sub not in result:
                    result.append(sub)
                return
            for i in range(len(candies)):
                if rst-candies[i]>=0:
                    bctk(candies[i:],sub+[candies[i]],rst-candies[i])
        
        bctk(candidates,[],target)
        return result