class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        for i in range(len(height)-1,0,-1):
            area=max(area,i*min(height[0],height[i]))
            if height[0]<height[-1]:
                height.pop(0)
            else:
                height.pop()
            
        return area
                
                