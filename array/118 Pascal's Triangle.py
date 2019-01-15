class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = res[i-1][j] + res[i-1][j-1]
            res.append(row)
        return res


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
