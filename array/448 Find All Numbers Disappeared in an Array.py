class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1
        # for i in range(len(nums)):
        #     index = i
        #     value = nums[i]
        #     while value != index + 1:
        #         tmp = nums[value - 1]
        #         nums[value - 1] = value
        #         index = value - 1
        #         value = tmp
        # return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]

        # Solution 2
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
