import java.util.HashMap;

class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        HashMap<Integer,Integer> map = new HashMap<>();
        return count(0,high,low,zero,one,map);
    }
    private int count(int len, int high, int low, int zero, int one, HashMap<Integer,Integer> map){
        if(len > high) return 0;
        int res = len >= low ? 1 : 0;
        if(map.containsKey(len)) return map.get(len);
        res += count(len+zero, high, low, zero, one, map) + count(len+one, high, low, zero, one, map);
        res = (int)(res%(1e9+7));
        map.put(len,res);
        return map.get(len);
    }
}