class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end=newInterval[0], newInterval[1]
        i=0
        out=[]
        boo=False
        while i< len(intervals) and intervals[i][1]<start:
            out.append(intervals[i])
            i+=1
        while i<len(intervals) and intervals[i][0]<=end:
            start=min(intervals[i][0],start)
            end=max(intervals[i][1],end)
            i+=1
        out.append([start,end])
        
        while i < len(intervals):
            out.append(intervals[i])
            i+=1
        return out