class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex):
            # j space store ith row
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res


if __name__ == "__main__":
    k = 33
    print(Solution().getRow(k))
