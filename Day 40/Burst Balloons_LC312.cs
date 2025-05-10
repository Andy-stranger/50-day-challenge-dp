public class Solution {
    public int MaxCoins(int[] nums) {
        var numList = new List<int>();
        numList.Add(1);
        numList.AddRange(nums.ToList());
        numList.Add(1);
        var dp = new List<List<int>>();
        for (int i = 0; i <= nums.Length+1; i++){
            var list = new List<int>();
            for (int j = 0; j <= nums.Length+1; j++) list.Add(0);
            dp.Add(list);
        }
        for(int i=nums.Length; i>0; i--){
            for(int j=1; j<=nums.Length; j++){
                if(i>j) continue;
                int max = int.MinValue;
                for(int k=i; k<=j; k++){
                    int cost = (numList[i-1]*numList[k]*numList[j+1])
                                + dp[i][k-1] + dp[k+1][j];
                    max = Math.Max(max, cost);
                }
                dp[i][j] = max;
            }
        }
        return dp[1][nums.Length];
    }
    // private int Fun(int i, int j, List<int> numList){
    //     if(i>j) return 0;
    //     int max = int.MinValue;
    //     for(int k=i; k<=j; k++){
    //         int cost = (numList[i-1]*numList[k]*numList[j+1])
    //                     + Fun(i, k-1, numList) + Fun(k+1, j, numList);
    //         max = Math.Max(max, cost);
    //     }
    //     return max;
    // }
}