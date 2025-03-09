def fibonacci_num(n):
    if n == 0 or n ==1:
        return n
    first = 0
    second = 1
    res = 0
    for i in range(2,n+1):
        res = first + second
        first = second
        second = res
    return res