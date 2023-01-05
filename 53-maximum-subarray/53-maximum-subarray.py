class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-10000
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            if pre>maxi:
                maxi=pre
            if pre<0:
                pre=0
        return maxi