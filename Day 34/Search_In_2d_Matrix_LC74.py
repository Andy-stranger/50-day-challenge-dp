def searchMatrix(self, matrix, target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    targetRow = -1
    top = 0
    bottom = rows-1
    while top <= bottom:
        mid = top + (bottom - top)//2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] <= target:
            targetRow = mid
            top = mid + 1
        else:
            bottom = mid - 1
    if targetRow != -1:
        left = 0
        right = cols - 1
        while left <= right:
            mid = left + (right - left)//2
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False