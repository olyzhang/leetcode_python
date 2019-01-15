class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # version 1:
        # result = []
        # points_dict = {}
        # for i in range(len(points)):
        #     points_dict[i] = points[i][0] ** 2 + points[i][1] ** 2
        # sorted_list = sorted(points_dict.items(), key = lambda x:x[1])
        # for i in range(K):
        #     result.append(points[sorted_list[i][0]])
        # return result

        # version 2
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]


if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(Solution().kClosest(points, K))
