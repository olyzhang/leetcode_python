class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        B = [[0] * rows for i in range(cols)]
        for i in range(cols):
            for j in range(rows):
                B[i][j] = A[j][i]
        return B


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().transpose(A))
