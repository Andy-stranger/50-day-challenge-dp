public class Solution {
    public int MaxProfit(int[] prices) {
        var prev = new int[5];
        var curr = new int[5];
        for(int ind=prices.Length-1; ind>=0; ind--){
            for(int cap=1; cap<=4; cap++){
                if(cap%2 == 0){
                    var buy = -prices[ind] + prev[cap-1];
                    var not_buy = prev[cap];
                    curr[cap] = Math.Max(buy, not_buy);
                }
                else{
                    var sell = prices[ind] + prev[cap-1];
                    var not_sell = prev[cap];
                    curr[cap] = Math.Max(sell, not_sell);
                }
            }
            prev = curr;
        }
        return prev[4];
    }
}