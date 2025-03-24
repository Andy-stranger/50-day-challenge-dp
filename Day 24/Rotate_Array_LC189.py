def rotate(nums, k: int) -> None:
    n = len(nums)
    if n == 0 or n == 1:
        return 
    k = k % n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]