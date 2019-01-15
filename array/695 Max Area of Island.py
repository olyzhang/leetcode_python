from queue import Queue


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Solution 1
        # max_area = 0
        # cur_area = 0
        # rows = len(grid)
        # cols = len(grid[0])
        # flags = [[0] * cols for i in range(rows)]
        # q = Queue()
        # for i in range(rows):
        #     for j in range(cols):
        #         if flags[i][j] == 0 and grid[i][j] == 1:
        #             q.put(i * cols + j)
        #             flags[i][j] = 1
        #             while not q.empty():
        #                 cur_index = q.get()
        #                 cur_area += 1
        #                 cur_row = cur_index // cols
        #                 cur_col = cur_index % cols
        #                 # print(cur_index)
        #                 # print(cur_row, " ", cur_col)
        #                 # print(cur_area)
        #                 if cur_row - 1 >= 0:
        #                     if flags[cur_row - 1][cur_col] == 0 and grid[cur_row - 1][cur_col] == 1:
        #                         q.put((cur_row - 1)*cols + cur_col)
        #                         flags[cur_row - 1][cur_col] = 1
        #                 if cur_row + 1 < rows:
        #                     if flags[cur_row + 1][cur_col] == 0 and grid[cur_row + 1][cur_col] == 1:
        #                         q.put((cur_row + 1)*cols + cur_col)
        #                         flags[cur_row + 1][cur_col] = 1
        #                 if cur_col - 1 >= 0:
        #                     if flags[cur_row][cur_col - 1] == 0 and grid[cur_row][cur_col - 1] == 1:
        #                         q.put((cur_row)*cols + cur_col - 1)
        #                         flags[cur_row][cur_col - 1] = 1
        #                 if cur_col + 1 < cols:
        #                     if flags[cur_row][cur_col + 1] == 0 and grid[cur_row][cur_col + 1] == 1:
        #                         q.put((cur_row)*cols + cur_col + 1)
        #                         flags[cur_row][cur_col + 1] = 1
        #             if cur_area > max_area:
        #                 max_area = cur_area
        #             cur_area = 0
        #         else:
        #             cur_area = 0
        # return max_area

        # Solution 2: dfs
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        return max(areas) if areas else 0


if __name__ == "__main__":
    grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    print(Solution().maxAreaOfIsland(grid))
