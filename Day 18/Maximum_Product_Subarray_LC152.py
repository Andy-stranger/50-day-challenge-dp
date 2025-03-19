def maxProduct(nums):
    n = len(nums)
    max_pdt = float("-inf")
    prefix = 1
    suffix = 1
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[n-i-1]
        max_pdt = max(max_pdt,max(prefix,suffix))
    return max_pdt