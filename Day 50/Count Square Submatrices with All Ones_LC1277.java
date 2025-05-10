class Solution {
    public int countSquares(int[][] matrix) {
        int sum = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] result = new int[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 || j==0 || matrix[i][j] == 0){
                    result[i][j] = matrix[i][j];
                }
                else{
                    result[i][j] = matrix[i][j] + Math.min(result[i-1][j], Math.min(result[i][j-1], result[i-1][j-1])); 
                }
                sum += result[i][j];
            }
        }
        return sum;
    }
}