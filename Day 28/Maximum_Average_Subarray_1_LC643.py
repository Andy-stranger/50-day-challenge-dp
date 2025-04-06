def findMaxAverage(self, nums, k: int) -> float:
    cur_sum = sum(nums[:k])
    left = 0
    right = k-1
    maxi = float("-inf")
    while(right < len(nums)):
        maxi = max(maxi , cur_sum)
        cur_sum -= nums[left]
        left += 1
        right += 1
        if right == len(nums):
            break
        cur_sum += nums[right]
        
    return maxi/k