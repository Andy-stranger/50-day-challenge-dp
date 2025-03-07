from typing import List

def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def recur(ind,curr,summ):
            if summ == n and len(curr) == k:
                res.append(curr[:])
                return
            for i in range(ind,10):
                curr.append(i)
                recur(i+1,curr,summ+i)
                curr.pop()
            return
        recur(1,[],0)
        return res