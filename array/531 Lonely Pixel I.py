class Solution(object):
    def findLonelyPixel(self, picture):
        h, w = len(picture), len(picture[0])
        rows, cols = [0] * h, [0] * w
        for i in range(h):
            for j in range(w):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(h):
            for j in range(w):
                if picture[i][j] == 'B':
                    if rows[i] == 1 and cols[j] == 1:
                        res += 1
        return res 


if __name__ == '__main__':
    picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]
    print(Solution().findLonelyPixel(picture))
