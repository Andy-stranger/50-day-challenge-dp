#Naive solution --> MLE
def Kth_Symbol_In_Grammer(n, curr, limit):
    if n == limit:
        curr = "".join(curr)
        return curr
    for i in range(len(curr)):
        if curr[i] == "0":
            curr[i] = "01"
        else:
            curr[i] = "10"
    curr = "".join(curr)
    curr = list(curr)
    return Kth_Symbol_In_Grammer(n+1, curr, limit)

n = int(input())
res = Kth_Symbol_In_Grammer(1, ["0"], n)
print(res)
k = int(input())
print(res[k-1])

#optimized solution
def Kth_Symbol_In_Grammer(n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2**(n-1)
        if k <= length//2:
            return Kth_Symbol_In_Grammer(n-1,k)
        else:
            return 1 - Kth_Symbol_In_Grammer(n-1,k-length//2)

n = int(input())
k = int(input())
print(Kth_Symbol_In_Grammer(n,k))