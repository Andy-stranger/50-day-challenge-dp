def tribonacci(self, n: int) -> int:
    if n == 0:
        return n
    if n == 1 or n == 2:
        return 1
    first = 0
    second = third = 1
    res = 0
    for i in range(3,n+1):
        res = first + second + third
        first = second
        second = third
        third = res
    return res