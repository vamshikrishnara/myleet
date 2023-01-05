class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while k < l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target and [nums[i],nums[j],nums[k],nums[l]] not in out:
                        out.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        l=l-1
                    elif nums[k]+nums[l]>(target-(nums[i]+nums[j])):
                        l=l-1
                    else:
                        k=k+1
        return out
                    