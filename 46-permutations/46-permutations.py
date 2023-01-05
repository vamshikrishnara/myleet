class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def bctq(q=0):
            if q==len(nums):
                output.append(nums[:])
            else:
                for i in range(q,len(nums)):
                    nums[q],nums[i]=nums[i],nums[q]
                    bctq(q+1)
                    nums[i],nums[q]=nums[q],nums[i]
        bctq()
        return output
                
                
                