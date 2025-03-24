def maxArea(height) -> int:
    n = len(height)
    left = 0
    right = n-1
    maxi = 0
    while left <= right:
        maxi = max(maxi,(right-left)*min(height[right],height[left]))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxi