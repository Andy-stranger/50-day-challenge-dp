public class Solution {
    public int IsPossible(int[] nums, int maxSum){
        int sum = 0;
        int count = 1;
        for(int i=0; i< nums.Length; i++){
            if(sum + nums[i] <= maxSum){
                sum += nums[i];
            }
            else{
                count++;
                sum = nums[i];
            }
        }
        return count;
    }
    public int SplitArray(int[] nums, int k) {
        int low = nums.Max();
        int high = nums.Sum();
        int mid = 0;
        while(low <= high){
            mid = (low+high)/2;
            if(IsPossible(nums, mid) > k) low = mid+1;
            else high = mid-1;
        }
        return low;
    }
}