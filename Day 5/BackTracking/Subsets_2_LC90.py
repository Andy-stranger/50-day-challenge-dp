from typing import List

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    def recur(ind,curr):
        if ind == len(nums):
            res.append(curr[:])
            return
        #take
        curr.append(nums[ind])
        take = recur(ind+1,curr)
        curr.pop() 
            
        #not take
        curVal = nums[ind]
        while ind < len(nums) and nums[ind] == curVal:
            ind += 1
        not_take = recur(ind,curr)
        return
    recur(0,[])
    return res