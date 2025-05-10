public class Solution {
    public int FindTheCity(int n, int[][] edges, int distanceThreshold) {
        int[,] matrix = new int[n,n];
        for(int r=0; r<n; r++){
            for(int c=0; c<n; c++){
                matrix[r,c] = r == c ? 0 : (int)1e9;
            }
        }
        foreach(var arr in edges){
            matrix[arr[0],arr[1]] = arr[2];
            matrix[arr[1],arr[0]] = arr[2];
        }
        for(int via=0; via<n; via++){
            for(int r=0; r<n; r++){
                for(int c=0; c<n; c++){
                    matrix[r,c] = Math.Min(matrix[r,c] , matrix[r,via] + matrix[via,c]);
                }
            }
        }
        var map = new Dictionary<int,int>();
        for(int r=0; r<n; r++){
            var temp = 0;
            for(int c=0; c<n; c++){
                if(matrix[r,c] <= distanceThreshold) temp++;
            }
            map.Add(r,temp);
        }
        var min = map.Values.Min();
        var res = map.Where(kvp => kvp.Value == min).Select(a => a.Key).ToList().Max();
        return res;
    }
}