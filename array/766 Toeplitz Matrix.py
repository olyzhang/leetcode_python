class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows-1):
            for j in range(1, cols):
                if matrix[i][j-1] != matrix[i+1][j]:
                    return False

        return True


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(Solution().isToeplitzMatrix(matrix))
