def  towerOfHanoi(self, n, fromm, to, aux):
    count = 0
    def recur(n,fromm,to,aux):
        nonlocal count
        if n == 0:
            return
        recur(n-1,fromm,aux,to)
        count += 1
        recur(n-1,aux,to,fromm)
        return
    recur(n,fromm,to,aux)
    return count