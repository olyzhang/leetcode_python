class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Solution 1
        # original_r = len(nums)
        # original_c = len(nums[0])
        # if original_c * original_r != r * c:
        #     return nums

        # new_nums = [[0] * c for i in range(r)]
        # tmp_r = 0
        # tmp_c = 0
        # for i in range(r):
        #     for j in range(c):
        #         new_nums[i][j] = nums[tmp_r][tmp_c]
        #         if tmp_c + 1 < original_c:
        #             tmp_c += 1
        #         else:
        #             tmp_r += 1
        #             tmp_c = 0
        # return new_nums

        # Solution 2:
        if r * c != len(nums) * len(nums[0]):
            return nums

        items = [y for x in nums for y in x]
        return [items[x * c:(x + 1) * c] for x in range(r)]


if __name__ == "__main__":
    nums = [[1, 2], [3, 4]]
    r = 4
    c = 1
    print(Solution().matrixReshape(nums, r, c))
