class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def isMagic(i, j):
            s = "".join(
                str(grid[i + x // 3][j + x % 3])
                for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and (s in "43816729" * 2
                                            or s in "43816729" [::-1] * 2)

        return sum(
            isMagic(i, j) for i in range(rows - 2)
            for j in range(cols - 2) if grid[i + 1][j + 1] == 5)


if __name__ == "__main__":
    grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    print(Solution().numMagicSquaresInside(grid))
