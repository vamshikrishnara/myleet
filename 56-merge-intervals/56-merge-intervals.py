class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        i=0
        intervals.sort()
        while i < len(intervals)-1:
            while i+1 < len(intervals) and intervals[i+1][0]<=intervals[i][1]:
                intervals[i]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals.pop(i+1)
            i+=1
        return intervals
                
            