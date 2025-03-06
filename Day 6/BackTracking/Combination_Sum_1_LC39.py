def combinationSum(candidates, target):
    res = []
    def recur(summ,curr,ind):
        if ind == len(candidates):
            return
        if summ == target:
            res.append(curr[:])
            return
        if summ + candidates[ind] <= target:
            summ += candidates[ind]
            curr.append(candidates[ind])
            recur(summ,curr,ind)
            curr.pop()
            summ -= candidates[ind]
        recur(summ,curr,ind+1)
        return
    recur(0,[],0)
    return res