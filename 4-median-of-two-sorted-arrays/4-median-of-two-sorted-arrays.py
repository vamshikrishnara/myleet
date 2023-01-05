class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        tot=m+n
        pos=tot//2
        count=0
        medi=[]
        i,j=0,0
        while count<pos+1:
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    medi.append(nums1[i])
                    count+=1
                    i+=1
                else:
                    medi.append(nums2[j])
                    count+=1
                    j+=1
            elif i<m:
                medi.append(nums1[i])
                count+=1
                i+=1
            else:
                medi.append(nums2[j])
                count+=1
                j+=1
        if tot%2==0:
            return (medi[len(medi)-1]+medi[len(medi)-2])/2
        return medi[len(medi)-1]
        
                        
                
                