def twoSum(self, numbers, target: int):
    n = len(numbers)
    left = 0
    right = n-1
    while left < right:
        summ = numbers[left] + numbers[right]
        if summ == target:
            return [left+1,right+1]
        if summ > target:
            right -= 1
        else:
            left += 1
    return []