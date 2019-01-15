class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """

    def maxDiff(self, arrs):
        # write your code here
        rows = len(arrs)
        res, start, end = 0, arrs[0][0], arrs[0][-1]
        for i in range(1, rows):
            res = max(res, abs(arrs[i][-1] - start), abs(arrs[i][0] - end))
            start = min(start, arrs[i][0])
            end = max(end, arrs[i][-1])
        return res


if __name__ == "__main__":
    arrs = [[1, 2, 3, 9], [4, 5], [1, 2, 3]]
    print(Solution().maxDiff(arrs))
