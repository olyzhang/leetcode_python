from math import floor


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(M), len(M[0])
        smooth_M = [[0] * cols for i in range(rows)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1],
                [-1, 1]]
        for i in range(rows):
            for j in range(cols):
                num, sum = 1, M[i][j]
                for k in range(8):
                    x, y = i + dirs[k][0], j + dirs[k][1]
                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        continue
                    sum += M[x][y]
                    num += 1
                smooth_M[i][j] = floor(sum / num)
        return smooth_M


if __name__ == "__main__":
    M = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution().imageSmoother(M))
