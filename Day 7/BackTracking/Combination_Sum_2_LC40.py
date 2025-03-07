from typing import List

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def recur(ind,summ,curr):
            if summ == target:
                res.append(curr[:])
                return
            if summ > target:
                return
            if ind == len(candidates):
                return
            mapp = {}
            for i in range(ind,len(candidates)):
                if candidates[i] not in mapp:
                    mapp[candidates[i]] = 1
                    curr.append(candidates[i])
                    recur(i+1,summ+candidates[i],curr)
                    curr.pop()
            return
        recur(0,0,[])
        return res