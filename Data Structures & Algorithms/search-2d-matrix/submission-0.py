class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m * n - 1
        
        while low <= high:
            mid = (low + high) // 2  # Use integer division
            row = mid // n  # Corrected to divide by 'n' (number of columns)
            col = mid % n  # Use modulus to get the column
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

        