class Solution {
    public int maxSubArray(int[] nums) {
        int maxsum=-99999;
        int check=0;
        for(int i=0;i<nums.length;i++){
            check+=nums[i];
            if (check > maxsum){
                maxsum=check;
            }
            if (check<0){
                check=0;
            }
        }
        return maxsum;
            
        
    }
}