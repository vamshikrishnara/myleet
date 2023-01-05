class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        out=9999
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target
                else:
                    if abs(target-(nums[i]+nums[j]+nums[k])) < abs(target-out):
                        out=nums[i]+nums[j]+nums[k]
                    if nums[j]+nums[k]>target-nums[i]:
                        k=k-1
                    else:
                        j=j+1
        return out