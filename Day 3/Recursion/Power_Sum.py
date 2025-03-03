def solve(arr):
    def recur(arr,p):
        summ = 0
        for i in arr:
            if type(i) == list:
                summ += solve(i,p+1)
            else:
                summ += i
        return summ**p
    return recur(arr,1)