class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out=[]
        queue=[]
        for i in range(len(nums)):
                queue.append([nums[i]])
        if len(queue)==1:
            out.append(nums)
            return out
        while len(queue)>0:
            v1=queue.pop(0)
            for i in range(len(nums)):
                if nums[i] in v1:
                    continue
                else:
                    if len(v1)+1==len(nums):
                        out.append(v1+[nums[i]])
                    else:
                        queue.append(v1+[nums[i]])
        return out
            
        
        
                
                
                