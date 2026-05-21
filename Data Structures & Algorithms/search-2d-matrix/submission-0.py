class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        left, bottom = 0, m - 1
        valid_row = -1

        while left <= bottom:
            mid = (left + bottom) // 2
            
            if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                valid_row = mid
                break;

            if matrix[mid][0] < target:
                left = mid + 1
            else:
                bottom = mid - 1
        
        
        if valid_row == -1:
            return False

        left, right = 0, n-1

        while left <= right:

            mid = (left + right) // 2

            if matrix[valid_row][mid] == target:
                return True

            if matrix[valid_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        
