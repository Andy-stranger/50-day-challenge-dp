from typing import List

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def recur(ind,curr):
        if ind == len(nums):
            res.append(curr[:])
            return
        #take
        curr.append(nums[ind])
        take = recur(ind+1,curr)
        
        #not take
        curr.pop()
        not_take = recur(ind+1,curr)
        return
    recur(0,[])
    return res