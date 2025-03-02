#Brute
def getSurvivor(n,k):
    def recur(curr,start,k):
        if len(curr) == 1:
            return curr[0]
        remove_ind = (start+k-1)%len(curr)
        curr.pop(remove_ind)
        return recur(curr,remove_ind,k)
    cur = []
    for i in range(n):
        cur.append(i+1)
    return recur(cur,0,k)

n = int(input())
k = int(input())
print(getSurvivor(n,k))

#Better
def getSurvivor(self, n: int, k: int) -> int:
    def recur(n,k):
        if n == 1:
            return 0
        return (recur(n-1,k)+k)%n
    return recur(n,k)+1

n = int(input())
k = int(input())
print(getSurvivor(n,k))

#Optimal
def getSurvivor(self, n: int, k: int) -> int:
    ans = 0
    for i in range(2,n+1):
        ans = (ans+k)%i
    return ans+1

n = int(input())
k = int(input())
print(getSurvivor(n,k))
