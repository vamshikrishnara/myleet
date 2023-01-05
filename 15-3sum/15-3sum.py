class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip=[]
        if len(nums)<3:
            return trip
        nums.sort()
        l=len(nums)
        for i in range(0,l):
            temp=0-nums[i]
            j=i+1
            k=l-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0 and [nums[i],nums[j],nums[k]] not in trip:
                    trip.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                elif nums[j]+nums[k]<temp:
                    j=j+1
                else:
                    k=k-1
        return trip
                
                