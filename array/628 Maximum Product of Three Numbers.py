class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # n = len(nums)
        # if n == 3:
        #     return nums[0] * nums[1] * nums[2]
        # max_non_negs = [0, 0, 0]
        # min_negs = [0, 0]
        # max_negs = [-10000, -10000, -10000]
        # negs_num, non_negs_num = 0, 0
        # for i in range(n):
        #     if nums[i] >= 0:
        #         non_negs_num += 1
        #         if nums[i] > max_non_negs[2]:
        #             max_non_negs[0] = max_non_negs[1]
        #             max_non_negs[1] = max_non_negs[2]
        #             max_non_negs[2] = nums[i]
        #         elif nums[i] > max_non_negs[1]:
        #             max_non_negs[0] = max_non_negs[1]
        #             max_non_negs[1] = nums[i]
        #         elif nums[i] > max_non_negs[0]:
        #             max_non_negs[0] = nums[i]
        #     else:
        #         negs_num += 1
        #         if nums[i] < min_negs[0]:
        #             min_negs[1] = min_negs[0]
        #             min_negs[0] = nums[i]
        #         elif nums[i] < min_negs[1]:
        #             min_negs[1] = nums[i]
        #         if nums[i] > max_negs[2]:
        #             max_negs[0] = max_negs[1]
        #             max_negs[1] = max_negs[2]
        #             max_negs[2] = nums[i]
        #         elif nums[i] > max_negs[1]:
        #             max_negs[0] = max_negs[1]
        #             max_negs[1] = nums[i]
        #         elif nums[i] > max_negs[0]:
        #             max_negs[0] = nums[i]

        # print(max_non_negs)
        # print(min_negs)
        # if negs_num <= 1:
        #     return max_non_negs[0] * max_non_negs[1] * max_non_negs[2]
        # elif non_negs_num == 0:
        #     return max_negs[0] * max_negs[1] * max_negs[2]
        # elif non_negs_num <= 2:
        #     return min_negs[0] * min_negs[1] * max_non_negs[2]
        # else:
        #     if max_non_negs[0] * max_non_negs[1] < min_negs[0] * min_negs[1]:
        #         return min_negs[0] * min_negs[1] * max_non_negs[2]
        #     else:
        #         return max_non_negs[0] * max_non_negs[1] * max_non_negs[2]

        # Solution 2
        n = len(nums)
        if n == 3:
            return nums[0] * nums[1] * nums[2]
        max1 = max2 = max3 = -10000
        min1 = min2 = 10000
        for i in range(n):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return max(max1 * max2 * max3, min1 * min2 * max1)


if __name__ == "__main__":
    nums = [
        722, 634, -504, -379, 163, -613, -842, -578, 750, 951, -158, 30, -238,
        -392, -487, -797, -157, -374, 999, -5, -521, -879, -858, 382, 626, 803,
        -347, 903, -205, 57, -342, 186, -736, 17, 83, 726, -960, 343, -984,
        937, -758, -122, 577, -595, -544, -559, 903, -183, 192, 825, 368, -674,
        57, -959, 884, 29, -681, -339, 582, 969, -95, -455, -275, 205, -548,
        79, 258, 35, 233, 203, 20, -936, 878, -868, -458, -882, 867, -664,
        -892, -687, 322, 844, -745, 447, -909, -586, 69, -88, 88, 445, -553,
        -666, 130, -640, -918, -7, -420, -368, 250, -786
    ]
    print(Solution().maximumProduct(nums))
