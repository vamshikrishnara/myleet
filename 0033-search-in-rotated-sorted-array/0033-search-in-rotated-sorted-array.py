class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        if nums[low]==target:
            return low
        if nums[high]==target:
            return high
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[high]:
                if nums[low] <= target and nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[low]>nums[mid]:
                if nums[mid]< target and target<nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return -1
            
             
        