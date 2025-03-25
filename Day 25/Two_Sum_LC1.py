def twoSum(nums, target: int):
    mapp = {}
    for ind,val in enumerate(nums):
        comp = target - val
        if comp in mapp:
            return [mapp[comp],ind]
        mapp[val] = ind
    return []