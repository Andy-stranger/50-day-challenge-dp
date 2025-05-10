import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int maxTwoEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[0] - b[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        int best = 0;
        for(var event : events){
            best = Math.max(best,event[2]);
        }
        int best_prev = Integer.MIN_VALUE;
        for(var event : events){
            while(!pq.isEmpty() && pq.peek()[0] < event[0]){
                var newVal = pq.poll();
                best_prev = Math.max(best_prev,newVal[1]);
            }
            pq.add(new int[]{event[1],event[2]});
            best = Math.max(best, best_prev + event[2]);
        }
        return best;
    }
}