class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        if len(nums)==0:
            return 0
            
        new=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=new:
                count=count+1
                new=nums[i]
                nums[count]=nums[i]
        return count+1
                